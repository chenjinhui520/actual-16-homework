
$('#editbtnclose').click(function(){
          $('#username').attr('value','')
          $('#email').attr('value','')
          $('#password').attr('value','')
          $('#rpassword').attr('value','')
})

$('#adduserbtn').click(function(){
	$('#useraddModal').modal('show')
        $('#newusername').change(function(){
		
                var username = $('#newusername').val().trim()
        
                type = 'POST'
                url = '/users/checkuser' 
                data = {username:username}
                
                function successfn5(data) {
            	    console.log(data)
            	    if (data['status'] == 1) {
                            $('#checknewuserinfo').html('This user exist. Please change another username!')
			    swal("Add user failed", "This user exist. Please change another user!")
			    //sweetAlert("This user exist. Please change another username", "出错了！","sucess");
            		    //$('#btnsave').attr('disabled',true)
            		    return false
            	    }
            	    else {
            	    console.log('user no exist')
                        $('#checknewuserinfo').html('')
        		console.log('enale disabled')
        		//$('#btnsave').attr('disabled',false)
            	    }
        
                }
                
                function errorfn5() {
            	    console.log('ajax error')
                        $('#newerrorstatus').html('Sorry. The server has an exception!')
		        swal("Error!", "The server has an exception!")
                }
        
                myajax(type,url,data,successfn5,errorfn5)
		
        
        })

	$('#btnnew').click(function(){
		console.log('new uesr btn')
		if ( !$("#add_user_form").valid() ) {
                  return
		}
                var username = $('#newusername').val().trim()
                var email = $('#newemail').val().trim()
                var password = $('#newpassword').val().trim()
                var rpassword = $('#newrpassword').val().trim()
		var role = $('#role').val()

		if ( password != rpassword ) {
                        $('#comparenewpasswd').html('The password and confirm password are different!')
			swal("Error!", "The password and confirm password are different!")
                        return
                }
                else {
                        $('#comparenewpasswd').html('')
                }


                type = 'POST'
                url = '/users/add'
                data = {username:username,email:email,password:password, role:role}

                function successfn6(data) {
			if ( data['status'] == 0 ) {
			        //alert('register success!')
			        swal("register success", "", "success")
                                location.reload()
			}
			else {
				//alert('register failed')
			        swal("register failed", "","error")
				location.reload()
			}
                }

                function errorfn6() {
                        $('#adderrorstatus').html('Add user failed. The server has an exception!')
		        swal("Error!", "The server has an exception","error")
                }
                myajax(type,url,data,successfn6 ,errorfn6)

	})


        
        $('#newemail').change(function(){
                var email = $('#newemail').val().trim()
        
                type = 'POST'
                url = '/users/checkemail' 
                data = {email:email}
        
                function successfn7(data) {
            	    if (data['status'] == 1) {
            	            $('#checknewemailinfo').html('This email exist. Please change another email!')
			    swal("email exist", "")
            		    //$('#btnsave').attr("disabled","true")
            		    return false
            	    }
            	    else {
            	        $('#checknewemailinfo').html('')
            		//$('#btnsave').attr("disabled","false")
            	    }
        
                }
                
                function errorfn7() {
                        $('#newerrorstatus').html('Sorry. The server has an exception!')
		        swal("Error!", "The server has an exception", "error")
                }
        
                myajax(type,url,data,successfn7, errorfn7)
        
        
        })
        
        
        $('#newrpassword').change(function(){
                var password = $('#newpassword').val().trim()
                var rpassword = $('#newrpassword').val().trim()
        
                if ( password != rpassword ) {
            	    $('#comparenewpasswd').html('The password and confirm password are different!')
		    swal("Error!", "The password and confirm password are different!", "error")
            	    return
                }
                else {
            	    $('#comparenewpasswd').html('')
                }
        
        
        })
})


$('.editbtn').click(function(){
        console.log('edit')
        var id = $(this).attr('uid')
        //var username = $(this).parents('tr').children('td').eq(1).text()
        //var email = $(this).parents('tr').children('td').eq(2).text()
        //var password = $(this).parents('tr').children('td').eq(3).text()

        type = 'POST'
        url = '/users/getuser/' + id
        data = {}

        function successfn3(data) {
		console.log(data)
                $('#username').attr('value',data['username'])
                $('#email').attr('value',data['email'])
                //$('#password').attr('value',data['password'])
                //$('#rpassword').attr('value',data['password'])
		role = data['role']
		if ( role == '' ) {
			role = User
		}
                $('#editrole').val( role)

        }

        function errorfn3() {
                $('#errorstatus').html('Sorry. The server has an exception!')
		swal("Error!", "The server has an exception", "error")
        }
        myajax(type,url,data,successfn3,errorfn3)

        $('#myModal').modal('show')

        //$('#username').attr('value',username.trim())
        //$('#email').attr('value',email.trim())
        //$('#password').attr('value',password.trim())
        //$('#rpassword').attr('value',password.trim())

	$('#btnsave').click(function(){
		if ( !$("#edit_user_form").valid() ) {
                  return
		}
                var username = $('#username').val().trim()
                var email = $('#email').val().trim()
                var password = $('#password').val().trim()
                var rpassword = $('#rpassword').val().trim()
		var role = $('#editrole').val().trim()

		if ( password != rpassword ) {
                        $('#comparepasswd').html('The password and confirm password are different!')
			$('#myModal').modal('hide')
			swal("Error!", "The password and confirm password are different!", "error")
			$('#myModal').modal('show')
                        return
                }
                else {
                        $('#comparepasswd').html('')
                }


                type = 'POST'
                url = '/users/edit/' + id
                data = {username:username,email:email,password:password,role:role,id:id}

                function successfn(data) {
		    swal("Edit success!", "", "success")
                    location.reload()
                }

                function errorfn() {
                        $('#errorstatus').html('Sorry. The server has an exception!')
		        swal("Error!", "The server has an exception", "error")
                }
                myajax(type,url,data,successfn,errorfn)

        })

        $('#username').change(function(){
                var username = $('#username').val().trim()
                console.log('username change')
        
        
                type = 'POST'
                url = '/users/checkuser' 
                data = {username:username}
                
                function successfn1(data) {
            	    console.log('successfn111111')
            	    console.log(data)
            	    if (data['status'] == 1) {
                            $('#checkuserinfo').html('This user exist. Please change another username!')
			    $('#myModal').modal('hide')
		            swal("This user exist", "", "error")
			    $('#myModal').modal('show')
            		  //  $('#btnsave').attr('disabled',true)
            		    return false
            	    }
            	    else {
            	    console.log('user no exist')
                        $('#checkuserinfo').html('')
        		//$('#btnsave').attr('disabled',false)
            	    }
        
                }
                
                function errorfn1() {
            	    console.log('ajax error')
                        $('#errorstatus').html('Sorry. The server has an exception!')
			$('#myModal').modal('hide')
			swal("Error!", "The password and confirm password are different", "error")
			$('#myModal').modal('show')
                }
        
                myajax(type,url,data,successfn1,errorfn1)
        
        })
        
        $('#email').change(function(){
                var email = $('#email').val().trim()
        
                type = 'POST'
                url = '/users/checkemail' 
                data = {email:email}
        
                function successfn2(data) {
            	    if (data['status'] == 1) {
            	            $('#checkemailinfo').html('This email exist. Please change another email!')
			    $('#myModal').modal('hide')
		            swal("This email exist", "", "error")
			    $('#myModal').modal('show')
            		    //$('#btnsave').attr("disabled","true")
            		    return false
            	    }
            	    else {
            	        $('#checkemailinfo').html('')
            		//$('#btnsave').attr("disabled","false")
            	    }
        
                }
                
                function errorfn2() {
                        $('#errorstatus').html('Sorry. The server has an exception!')
			$('#myModal').modal('hide')
			swal("Error!", "The password and confirm password are different", "error")
			$('#myModal').modal('show')
                }
        
                myajax(type,url,data,successfn2,errorfn2)
        
        
        })
        
        
        $('#rpassword').change(function(){
                var password = $('#password').val().trim()
                var rpassword = $('#rpassword').val().trim()
        
                if ( password != rpassword ) {
            	    $('#comparepasswd').html('The password and confirm password are different!')
		    $('#myModal').modal('hide')
		    swal("Error!", "The password and confirm password are different", "error")
		    $('#myModal').modal('show')
            	    return
                }
                else {
            	    $('#comparepasswd').html('')
                }
        
        
        })

})
          

$('.delbtn').click(function(){
    $('#myDelModal').modal('show')
    var uid = $(this).attr('uid')
    var name = $(this).attr('username')
    $('#delinfo').html('你确定要删除 ' + name + ' 用户吗?')

    $('#btndel').click(function(){

    	    type = 'POST'
    	    url = '/users/del/' + uid
    	    data = {}
    	    function successfn4(data) {
		    swal("success!","Delete successfully!", "success")
                    
    	            location.reload()

    	    }
    	    
    	    function errorfn4() {
		    swal("Delete failed", "ajax error", "error")
    		    console.log('del ajax error')
    	    }

            myajax(type,url,data,successfn4, errorfn4)

    })
       
})

