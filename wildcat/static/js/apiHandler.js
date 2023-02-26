function starHandler(state, count, product_id) {
    return {
        state: state,
        count: count,
        svgOutline: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full"><path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z" /></svg>',
        svgSolid: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-full h-full"><path fill-rule="evenodd" d="M10.788 3.21c.448-1.077 1.976-1.077 2.424 0l2.082 5.007 5.404.433c1.164.093 1.636 1.545.749 2.305l-4.117 3.527 1.257 5.273c.271 1.136-.964 2.033-1.96 1.425L12 18.354 7.373 21.18c-.996.608-2.231-.29-1.96-1.425l1.257-5.273-4.117-3.527c-.887-.76-.415-2.212.749-2.305l5.404-.433 2.082-5.006z" clip-rule="evenodd" /></svg>',
        currentSvg: '',
        init() {
            this.changeSvg()
        },
        changeSvg() {
            if (this.state) {
                this.currentSvg = this.svgSolid
            } else {
                this.currentSvg = this.svgOutline
            }
        },
        changeStar() {
            this.makeRequest()
            if (this.state) {
                this.count--
            } else {
                this.count++
            }
            this.state = !this.state
            this.changeSvg()
        },
        makeRequest() {
            // let method = ''
            this.state ? method = 'DELETE' : method = 'PUT'
            fetch(`/api/products/star/${product_id}`, {method: method, headers: {"X-CSRFToken": this.getCookie('csrftoken')}})
        },
        getCookie(name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        }
    }
}

function followHandler(state, count, user_id) {
    return {
        state: state,
        count: count,
        svgOutline: '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" /></svg>',
        svgSolid: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-full h-full"><path d="M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z" /></svg>',
        currentSvg: '',
        init() {
            this.changeSvg()
        },
        changeSvg() {
            if (this.state) {
                this.currentSvg = this.svgSolid
            } else {
                this.currentSvg = this.svgOutline
            }
        },
        changeFollow() {
            this.makeRequest()
            if (this.state) {
                this.count--
            } else {
                this.count++
            }
            this.state = !this.state
            this.changeSvg()
        },
        makeRequest() {
            this.state ? method = 'DELETE' : method = 'PUT'
            fetch(`/api/accounts/follow/${user_id}`, {method: method, headers: {"X-CSRFToken": this.getCookie('csrftoken')}})
        },
        getCookie(name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        }
    }
}