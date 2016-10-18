var log = function() {
  console.log(arguments)
}

var bindEventMsg = function() {
    // 给按钮绑定添加 评论 事件
    $('.a-msgs-link').on('click', function(){
      // 得到并且生成 form 数据
      var id = $(this).data('id');

      // 这个响应函数会在 AJAX 调用完成后被调用
      var response = function(r) {
          var t = r.data
          var blog_id = t.blog_id
          log('debug blog_id, ', blog_id)
          window.location.href = "http://localhost:3000/" + blog_id
          /*
          这个函数会被 weiboAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 字典形式数据,
              'message': 错误消息
          }
          */

      }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 event.js
      // 所以 event.js 里面可以使用 api.js 中的内容
      api.msg(id, response)
    })
}

var bindEvents = function() {
    // 不同的事件用不同的函数去绑定处理
    // 这样逻辑就非常清晰了
    bindEventMsg()
}

// 页面载入完成后会调用这个函数，所以可以当做入口
$(document).ready(function(){
    // 用 bindEvents 函数给不同的功能绑定事件处理
    // 这样逻辑就非常清晰了
    bindEvents()
})
