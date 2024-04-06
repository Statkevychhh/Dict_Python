new Vue({
    el: '#order_app',
    data: {
        orders: []
    },
    created: function () {
        const vn = this;
        axios.get('/api/orders/')
        .then(function (response){
        vm.orders = response.data
        })
    }
}

)