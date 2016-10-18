var log = function() {
  console.log(arguments)
}

// 这个函数用来根据 评论 对象生成一条评论的 HTML 代码
var todoTemplate = function(todo) {
  var c = todo
  var td = `
    <div class="class-div-comment-reply">
        <div>
            用户名：${ c.username }  创建时间：${ c.created_time }  内容：${ c.content }
            <span class="class-span-comment-reply">回复</span>
        </div>
        <div class="class-div-comment-reply" style="display: none" data-id=${ c.id }>
            <textarea name="content"></textarea>
            <button class="class-button-comment-reply">发布</button>
        </div>
    </div>
    <div class="bbs-replys">
    </div>
  `
  return td
}

var bindEventCommentToggle = function(){
    // 展开评论事件
    $('body').on('click', '#id-span-blog-comment', function(){
        $(this).parent().parent().find('#id-div-blog-comment').slideToggle()
        // 因为展开评论是一个超链接 a 标签
        // 所以需要 return false 来阻止它的默认行为
        // a 的默认行为是跳转链接，没有指定 href 的时候就跳转到当前页面
        // 所以需要阻止
        //return false;
    })
}

var bindEventAdd = function() {
    // 给按钮绑定添加 点赞 事件
    $('#id-span-blog-add').on('click', function(){
      // 得到点赞数并且生成 form 数据
      var blogId = $(this).parent().data('id');
      var up_count = $('#id-span-blog-upcount');
      var upcount = up_count.text();
      var form = {
        blogId: blogId,
        upcount: upcount,
      }

      // 这个响应函数会在 AJAX 调用完成后被调用
      var response = function(r) {
          /*
          这个函数会被 weiboAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 数据,
              'message': 错误消息
          }
          */
          // arguments 是包含所有参数的一个 list
          console.log('成功', arguments)
          log(r)
          if(r.success) {
              // 如果成功就添加到页面中
              // 因为添加微博会返回已添加的微博数据所以直接用 r.data 得到
              var t = r.data
              $(up_count).text(t.upcount)
              alert("点赞成功")
          } else {
              // 失败，弹出提示
              alert(r.message)
          }
      }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 event.js
      // 所以 event.js 里面可以使用 api.js 中的内容
      api.blogUp(form, response)
    })
}

var bindEventDel = function() {
    // 给按钮绑定添加 扔蛋 事件
    $('#id-span-blog-del').on('click', function(){
      // 得到点赞数并且生成 form 数据
      var blogId = $(this).parent().data('id');
      var down_count = $('#id-span-blog-downcount');
      var downcount = down_count.text();
      var form = {
        blogId: blogId,
        downcount: downcount,
      }

      // 这个响应函数会在 AJAX 调用完成后被调用
      var response = function(r) {
          /*
          这个函数会被 weiboAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 数据,
              'message': 错误消息
          }
          */
          // arguments 是包含所有参数的一个 list
          console.log('成功', arguments)
          log(r)
          if(r.success) {
              // 如果成功就添加到页面中
              // 因为添加微博会返回已添加的微博数据所以直接用 r.data 得到
              var t = r.data
              $(down_count).text(t.downcount)
              alert("扔蛋成功")
          } else {
              // 失败，弹出提示
              alert(r.message)
          }
      }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 event.js
      // 所以 event.js 里面可以使用 api.js 中的内容
      api.blogDown(form, response)
    })
}

var bindEventCommentAdd = function() {
    // 给按钮绑定添加 评论 事件
    $('#id-button-blog-comment').on('click', function(){
      // 得到点赞数并且生成 form 数据
      var blogId = $(this).parent().data('id');
      var temp = $(this).parent().find("textarea");
      var content = $(temp).val();
      var form = {
        blogId: blogId,
        content: content,
      }

      // 这个响应函数会在 AJAX 调用完成后被调用
      var response = function(r) {
          /*
          这个函数会被 weiboAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 字典形式数据,
              'message': 错误消息
          }
          */
          // arguments 是包含所有参数的一个 list
          console.log('成功', arguments)
          log(r)
          if(r.success) {
              // 如果成功就添加到页面中
              // 因为添加微博会返回已添加的微博数据所以直接用 r.data 得到
              var t = r.data
              $('.bbs-comments').append(todoTemplate(t))
              $(temp).val('')
              $('#id-div-blog-comment').slideToggle()
              alert("评论成功")
          } else {
              // 失败，弹出提示
              alert(r.message)
          }
      }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 event.js
      // 所以 event.js 里面可以使用 api.js 中的内容
      api.blogComment(form, response)
    })
}

// 这个函数用来根据 评论 对象生成一条评论的 HTML 代码
var replyTemplate = function(todo) {
  var r = todo
  var td = `
    <div>
        <img src="${ r.avatar }" width="50px" height="50px">${ r.username }${ r.created_time }<br/>
        ${ r.content }
    </div>
  `
  return td
}

var bindEventReplyToggle = function(){
    // 展开回复评论事件
    $('body').on('click', '.class-span-comment-reply', function(){
        $(this).parent().next('.class-div-comment-reply').slideToggle()
        // 因为展开评论是一个超链接 a 标签
        // 所以需要 return false 来阻止它的默认行为
        // a 的默认行为是跳转链接，没有指定 href 的时候就跳转到当前页面
        // 所以需要阻止
        //return false;
    })
}

var bindEventReplyAdd = function() {
    // 给按钮绑定添加 评论 事件
    $('body').on('click', '.class-button-comment-reply', function(){
      // 得到并且生成 form 数据
      var CommentId = $(this).parent().data('id');
      var temp = $(this).parent().find("textarea");
      var reply = $(this).parents('.class-div-comment-reply').next(".bbs-replys")
      log('debug reply, ', reply)
      var tog = $(this).parent()
      var content = $(temp).val();
      var form = {
        CommentId: CommentId,
        content: content,
      }

      // 这个响应函数会在 AJAX 调用完成后被调用
      var response = function(r) {
          /*
          这个函数会被 weiboAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 字典形式数据,
              'message': 错误消息
          }
          */
          // arguments 是包含所有参数的一个 list
          console.log('成功', arguments)
          log(r)
          if(r.success) {
              // 如果成功就添加到页面中
              // 因为添加微博会返回已添加的微博数据所以直接用 r.data 得到
              var t = r.data
              $(reply).append(replyTemplate(t))
              $(temp).val('')
              $(tog).slideToggle()
              alert("评论成功")
          } else {
              // 失败，弹出提示
              alert(r.message)
          }
      }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 event.js
      // 所以 event.js 里面可以使用 api.js 中的内容
      api.commentReply(form, response)
    })
}

var bindEvents = function() {
    // 不同的事件用不同的函数去绑定处理
    // 这样逻辑就非常清晰了
    bindEventCommentToggle()
    bindEventReplyToggle()
    bindEventAdd()
    bindEventDel()
    bindEventCommentAdd()
    bindEventReplyAdd()
}

// 页面载入完成后会调用这个函数，所以可以当做入口
$(document).ready(function(){
    // 用 bindEvents 函数给不同的功能绑定事件处理
    // 这样逻辑就非常清晰了
    bindEvents()
})
