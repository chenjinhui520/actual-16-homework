
//验证表单
$("#addform").validate();


//-----------添加用户模态框开始-------------
$('.regbtn').click(function(){
    // 弹起模态框
    $('#myModal').modal('show')

        //判断用户名是否已存在start
        $('#name').change(function(){
            username = $('#name').val()
            retdata = {"username":username}
            $.post("/users/checkusername", retdata, function(data){
                console.log(data.status)
                if (data.status == 1){
                    sweetAlert("哎呦……", "用户名已存在，请更换用户名！","error");
                };
            });
        })

       // 点击模态框的保存按钮，发送数据到后端 完成修改
       $('#btnsave').click(function(){
         if (!$("#user_add_form").valid() ) {
             return ;
           } else {

       // 获取模态框修改后的值
       username = $('#name').val()
       passwd = $('#passwd').val()
       rpasswd = $('#rpasswd').val()
       email = $('#email').val()
       role= $('#role').val()

       if (passwd != rpasswd ){
           swal("两次输入的密码不一致", "重新输入")
           return false
           };

           retdata = {"username":username,"password":passwd, "email":email,"role":role}
           $.post("/users", retdata, function(data){
                   location.reload()
                })
             swal("注册成功！", "","success")

   }
             })
              })
//---------------添加用户模态框js结束---------------


//-----------修改用户的模态框start-------------------
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
        role= $('#role').val()
        console.log(role)

        if (passwd != rpasswd ){
             $('.pwdmsg').html('两次输入的密码不一致，请重新输入！')
             return false
         }
        else{
             $('.pwdmsg').hide()
        }

    	data = {"username":username,"password":passwd, "email":email, "id":id,"role":role }
	    console.log(data)
           $.post("/users/edit", data, function(data){
                   location.reload()
           });

        })
    })
//---------修改用户的模态框结束--------------

