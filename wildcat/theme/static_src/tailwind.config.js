/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'class',
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/*.html',
        '../../templates/**/*.html',
        '../../templates/**/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        colors: {
            'bgcol-l': '#f9f9f9',
            'bgcol-d': '#1a1a1a',
            'navhov-l': '#487528',
            'navhov-d': '#5f9933',
            'scroll-l': '#292929',
            'scroll-d': '#5d5d5d',
            'con-l': '#ececec',
            'con-d': '#272727',
            'form-l': '#dddddd',
            'form-d': '#414141',
            'green-l': '#6aa93b',
            'green-d': '#649d39',
            'green-hov': '#5b9033',
            'white': '#ffffff',
            'black': '#000000',
            'slate': {
                300: '#cbd5e1',
                500: '#64748b',
                900: '#0f172a',
            },
        },
        screens: {
            'sm': {'min': '200px', 'max': '767px'},
            // => @media (min-width: 640px and max-width: 767px) { ... }
      
            'md': {'min': '768px', 'max': '1023px'},
            // => @media (min-width: 768px and max-width: 1023px) { ... }
      
            'lg': {'min': '1024px', 'max': '1279px'},
            // => @media (min-width: 1024px and max-width: 1279px) { ... }
      
            'xl': {'min': '1280px', 'max': '1535px'},
            // => @media (min-width: 1280px and max-width: 1535px) { ... }
      
            '2xl': {'min': '1536px'},
            // => @media (min-width: 1536px) { ... }
          },
        extend: {
            backgroundImage: {
                'Light': "url('/static/img/topography-light.svg')",
                'Dark': "url('/static/img/topography-dark.svg')",
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('tailwind-scrollbar')({ nocompatible: true }),
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
    variants: {
        scrollbar: ['rounded']
    }
}
