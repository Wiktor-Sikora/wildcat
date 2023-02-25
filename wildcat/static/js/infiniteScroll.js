function infinityScroll() {
  return {
    product_name: '',
    product_owner: '',
    open: false,
    loader: true,
    page: '',
    products: [],
    getUrl() {
      this.page = `/api/products?format=json&name=${this.product_name}&owner=${this.product_owner}&tags=`
    },
    getItems() {
      fetch(this.page)
        .then(response => {
          if (response.status === 404) {
            console.log('end')
          } else {
            return response.json()
          }
        }).then(data => {
          this.products = this.products.concat(data.results)
          if (data.next == null) {
            this.loader = false
          } else {
            this.page = data.next
            this.loader = true
          }
        })
    },
    clearItems() {
      this.products = []
    }
  }
}