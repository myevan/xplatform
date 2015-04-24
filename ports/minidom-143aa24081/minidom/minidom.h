/*

    minidom - a minimized dom/path library
    See README for copyright and license information.

*/

#ifndef _MINIDOM_H_
#define _MINIDOM_H_

/*
 *
 * If you don't use cmake, 
 *
 * define MINIDOM_SUPPORT_XML to parse XML
 * define MINIDOM_SUPPORT_INI to parse INI
 * define MINIDOM_SUPPORT_JSON to parse JSON
 * define MINIDOM_SUPPORT_NKV to parse NKV
 * define MINIDOM_SUPPORT_HTTP to parse HTTP header
 * define MINIDOM_SUPPORT_PHP to parse PHP serialized object
 *
 * define MINIDOM_ENABLE_DUMP to dump(save) dom into text or file
 * define MINIDOM_ENABLE_ICONV to use iconv library
 * define MINIDOM_DEBUG to show stl types on debugging
 *
 *
 */

#if defined(_WIN32) || defined(_WIN64)
    #define MINIDOM_PLATFORM_WINDOWS
#elif defined(linux) || defined(__linux) || defined(__linux__)
    #define MINIDOM_PLATFORM_LINUX
#elif defined(__FreeBSD__)
    #define MINIDOM_PLATFORM_BSD
#elif defined(macintosh) || defined(__APPLE__) || defined(__APPLE_CC__)
    #define MINIDOM_PLATFORM_MACOS
#else
    // TODO: So, what is your platform?
#endif

#if defined( MINIDOM_PLATFORM_WINDOWS )
    #if defined( MINIDOM_DLL )
        #if defined( MINIDOM_EXPORT )
            #define MINIDOM_API __declspec(dllexport)
        #else
            #define MINIDOM_API __declspec(dllimport)
        #endif
    #else
        #define MINIDOM_API
    #endif /* MINIDOM_DLL */
#else /* other platforms */
    #define MINIDOM_API
#endif /* MINIDOM_PLATFORM_WINDOWS */

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

#ifdef MINIDOM_ENABLE_ICONV
    #if defined(MINIDOM_PLATFORM_WINDOWS)
        #include "../requisite/libiconv/include/iconv.h"
    #else
        #include <iconv.h>
    #endif
#endif

namespace minidom
{
    class MINIDOM_API node;
    class MINIDOM_API selector;
    class MINIDOM_API doc;
    class MINIDOM_API algorithm;

    typedef std::vector<node*> NodeVec;
    typedef std::vector<node*>::iterator NVI;

    class MINIDOM_API algorithm
    {
        friend class node;
        friend class selector;
    private:
        static bool compare(
                const std::string& dst,
                const std::string& src,
                size_t jump = 0 );
        static bool reverse_compare(
                const std::string& dst,
                const std::string& src,
                size_t jump = 0 );
    };

    class MINIDOM_API node
    {
        friend class doc;
        friend class selector;
    public:
        node* parent() { return parent_; }
        node* next() { return next_; }
        node* prev() { return prev_; }
        node* firstChild();
        node* lastChild();
        node* firstAttr();
        node* lastAttr();

        node* get( const std::string& path, size_t no = 0 );
        size_t size( bool cascade = false );
        size_t count( const std::string& path );
        /* 'print' function is not safe on dynamic library.
            use it with your own risk. */
        void print( std::ostream& stream = std::cout, 
                bool useIndent = true, size_t indent = 0 );

        node* add( const char* k, const char* v = NULL, bool bAttribute = false );
        node* add( const char* k, int v, bool bAttribute = false );
        node* add( const char* k, double v, bool bAttribute = false );

        node* add( const std::string& k, const std::string& v = "", bool bAttribute = false );
        node* add( const std::string& k, int v, bool bAttribute = false );
        node* add( const std::string& k, double v, bool bAttribute = false );

        const std::string& toKey() { return k_; }
        const std::string& toValue() { return v_; }
        const std::string& topath() { return path_; }

        std::string& toString();
        const char* toChars();
        int toInt();
        double toDouble();
        void clear();

    protected:
        node();
        virtual ~node();
        void addChild( node* child );
        void addAttr( node* attr );
        virtual node* getNode( const std::string& path, size_t no = 0, bool getCount = false );

        std::string path_;
        std::string k_;
        std::string v_;
        bool array_;

        doc* doc_;
        node* parent_;
        node* prev_;
        node* next_;
        NodeVec attrVec_;
        NodeVec childVec_;
    };

    class MINIDOM_API selector
    {
        friend class doc;
    public:
        selector();
        virtual ~selector();

    public:
        selector& query( const std::string& query );
        int query( const std::string& query, selector* s );
        node* at( size_t i );
        void printResult( std::ostream& stream = std::cout );
        size_t size();

    protected:
        NodeVec nodeVec_;
    };

    class MINIDOM_API doc : public node, public selector
    {
        friend class node;
    public:
        enum DOCTYPE {
            XML,
            INI,
            JSON,
            NKV,
            HTTP,
        };

    public:
        doc();
        virtual ~doc();

    public:
        size_t size();
        int loadString( DOCTYPE type, 
                const char* text, 
                const std::string targetEncoding = "" );
        int loadFile( DOCTYPE type, 
                const std::string& filename, 
                const std::string targetEncoding = "" );    
        int dumpString( DOCTYPE type, 
                char* target,
                size_t* size,
                const std::string targetEncoding = "" );
        int dumpFile( DOCTYPE type, 
                const std::string& filename, 
                const std::string targetEncoding = "" );

    protected:
        int parseXML( const char* text );
        int parseINI( const char* text );
        int parseJSON( const char* text );
        int parseNKV( const char* text );
        int parseHTTP( const char* text );

        int writeXML( char* buf, size_t* size, void* conv );
        int writeINI( char* buf, size_t* size, void* conv );
        int writeJSON( char* buf, size_t* size, void* conv );
        int writeNKV( char* buf, size_t* size, void* conv );
        int writeHTTP( char* buf, size_t* size, void* conv );

        int initIconv();
        void* iconv_;
        inline std::string& convertString( std::string& str );
        std::string srcEncoding_;
        std::string dstEncoding_;
    };
}

#endif /* _MINIDOM_H_ */
