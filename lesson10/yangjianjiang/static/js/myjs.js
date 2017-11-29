//ajax 函数start
function myajax(type,url,data,sfunc,efunc){
    $.ajax({
    type:type,
    url:url,
    data:data,
    dataType:"json",
    success:function(data){
        sfunc(data)
    },
    error:function(){
        efunc()
    },
    })
}
//ajax 函数END

//添加用户模态框开始
$('.regbtn').click(function(){
    
    // 弹起模态框
    $('#myModal').modal('show')
        //判断用户名是否已存在start
        $('#name').change(function(){
            username = $('#name').val()
            console.log('hahaha')
            type = 'POST'
            url = '/checkusername'
            data = {"username":username}
            function sf1(data){
                if (data.status == 1){
                    $('.namemsg').html('输入的用户名已存在，请更换用户名！')
                    }
                else{
                    $('.namemsg').hide()
                    }
                }
            function ef1(){
                } 
            myajax(type,url,data,sf1,ef1)                
        })
        //判断用户名是否存在END

       // 点击模态框的保存按钮，发送数据到后端 完成修改
       $('#btnsave').click(function(){

       // 获取模态框修改后的值
       username = $('#name').val()
       passwd = $('#passwd').val()
       rpasswd = $('#rpasswd').val()
       email = $('#email').val()

              //判断两次输入密码是否一致
              if (username == ""){
                   $('.namemsg').html('用户名不能为空！')
                   return false
              }
              else{
                   $('.namemsg').hide()

              }
              if( passwd == ""){
                   $('.pwdmsg').html('密码不能为空！')
                   return false
              }
              else{
                   $('.pwdmsg').hide()

              }
              if (email == ""){
                   $('.emailmsg').html('邮箱不能为空！')
                   return false
              }
              else{
                   $('.emailmsg').hide()

              }

              if (passwd != rpasswd ){
                   $('.pwdmsg').html('两次输入的密码不一致，请重新输入！')
                   return false
               }
              else{
                   $('.pwdmsg').hide()
              }

           type = 'POST'    // GET,POST,DELETE,PUT, ...
           url = '/users'
           data = {username:username,password:passwd, email:email }
           console.log(data)
           function sf1(data){
               location.reload()
                }
            function ef1(){
                } 
            myajax(type,url,data,sf1,ef1)                

             })
              })
     //添加用户模态框js结束


    //修改用户的模态框start
	$('.editbtn').click(function(){
		// 获取table编辑按钮这一行的 用户名 邮箱 密码 的值
		id = $(this).attr('uid')
		var username = $(this).parents("tr").children("td").eq(1).text()
		var passwd = $(this).parents("tr").children("td").eq(2).text()
		var rpasswd = $(this).parents("tr").children("td").eq(2).text()
		var email = $(this).parents("tr").children("td").eq(3).text()

		// 弹起模态框
		$('#myModal').modal('show')

		// 把值写入模态框的各个input
		$('#name').attr('value', username.trim())
		$('#passwd').attr('value', passwd.trim())
		$('#rpasswd').attr('value', rpasswd.trim())
		$('#email').attr('value', email.trim())

		// 点击模态框的保存按钮，发送数据到后端 完成修改
		$('#btnsave').click(function(){

		// 获取模态框修改后的值
		username = $('#name').val()
		passwd = $('#passwd').val()
		rpasswd = $('#rpasswd').val()
		email = $('#email').val()

        if (username == ""){
           $('.namemsg').html('用户名不能为空！')
           return false
          }
         else{
             $('.namemsg').hide()

        }
        if( passwd == ""){
             $('.pwdmsg').html('密码不能为空！')
             return false
        }
        else{
             $('.pwdmsg').hide()

        }
        if (email == ""){
             $('.emailmsg').html('邮箱不能为空！')
             return false
        }
        else{
             $('.emailmsg').hide()

        }

        if (passwd != rpasswd ){
             $('.pwdmsg').html('两次输入的密码不一致，请重新输入！')
             return false
         }
        else{
             $('.pwdmsg').hide()
        }

		type = 'POST'    // GET,POST,DELETE,PUT, ...
    	url = '/users/edit'
    	data = {username:username,password:passwd, email:email, id:id }
	    console.log(data)

           function sf1(data){
               location.reload()
                }
            function ef1(){
                } 
            myajax(type,url,data,sf1,ef1)                

        })
    })
    //修改用户的模态框结束

