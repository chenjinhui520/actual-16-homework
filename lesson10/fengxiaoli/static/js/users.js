
function checkuser(username){
        if ( username == '' ) {
                $('#checkuserinfo').html('Username is null')
                return false
        }
        else {
                $('#checkuserinfo').html('')
        }
        return true
}

function checkemail(email){
        if ( email == '' ) {
                $('#checkemailinfo').html('Email is null')
                return false
        }
        else {
                $('#checkemailinfo').html('')
        }

        var re =  /^(\w)+(\.\w+)*@51reboot\.com$/;
        if (!re.test(email)) {
               $('#checkemailinfo').html('This email format is not correct. Please use *@51reboot\.com.')
               return false

        }
        return true

}

function checkpasswd(password){
        if ( password == '' ) {
                $('#checkpasswd').html('Password is null')
                return false
        }
        else {
                $('#checkpasswd').html('')
        }
        return true
}

function checkrpasswd(rpassword){
        if ( rpassword == '' ) {
                $('#comparepasswd').html('Confirm password is null')
                return false
        }
        else {
                $('#comparepasswd').html('')
        }
        return true
}


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
        
                if (!checkuser(username))
            	    return
        
                type = 'POST'
                url = '/checkuser' 
                data = {username:username}
                
                function successfn5(data) {
            	    console.log(data)
            	    if (data['status'] == 1) {
                            $('#checknewuserinfo').html('This user exist. Please change another username!')
            		  //  $('#btnsave').attr('disabled',true)
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
                }
        
                myajax(type,url,data,successfn5,errorfn5)
		
        
        })

	$('#btnnew').click(function(){
		console.log('new uesr btn')
                var username = $('#newusername').val().trim()
                var email = $('#newemail').val().trim()
                var password = $('#newpassword').val().trim()
                var rpassword = $('#newrpassword').val().trim()

                if (!checkuser(username))
                            return

                if (!checkemail(email))
                    return

                if (!checkpasswd(password))
                    return

                if (!checkrpasswd(rpassword))
                    return
		if ( password != rpassword ) {
                        $('#comparenewpasswd').html('The password and confirm password are different!')
                        return
                }
                else {
                        $('#comparenewpasswd').html('')
                }


                type = 'POST'
                url = '/users/add'
                data = {username:username,email:email,password:password}

                function successfn6(data) {
			if ( data['status'] == 0 ) {
			        alert('register success!')
                                location.reload()
			}
			else {
				alert('register failed')
				location.reload()
			}
                }

                function errorfn6() {
                        $('#adderrorstatus').html('Add user failed. The server has an exception!')
                }
                myajax(type,url,data,successfn6 ,errorfn6)

	})


        
        $('#newemail').change(function(){
                var email = $('#newemail').val().trim()
                if (!checkemail(email))
            	    return
        
                type = 'POST'
                url = '/checkemail' 
                data = {email:email}
        
                function successfn7(data) {
            	    if (data['status'] == 1) {
            	            $('#checknewemailinfo').html('This email exist. Please change another email!')
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
                }
        
                myajax(type,url,data,successfn7, errorfn7)
        
        
        })
        
        $('#newpassword').change(function(){
                var password = $('#newpassword').val().trim()
                if (!checkpasswd(password))
            	    return
        
        })
        
        $('#newrpassword').change(function(){
                var password = $('#newpassword').val().trim()
                var rpassword = $('#newrpassword').val().trim()
                if (!checkrpasswd(rpassword))
            	    return
        
                if ( password != rpassword ) {
            	    $('#comparenewpasswd').html('The password and confirm password are different!')
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
        url = '/getuser/' + id
        data = {}

        function successfn3(data) {
		console.log(data)
                $('#username').attr('value',data['username'])
                $('#email').attr('value',data['email'])
                $('#password').attr('value',data['password'])
                $('#rpassword').attr('value',data['rpassword'])
        }

        function errorfn3() {
                $('#errorstatus').html('Sorry. The server has an exception!')
        }
        myajax(type,url,data,successfn3,errorfn3)

        $('#myModal').modal('show')

        //$('#username').attr('value',username.trim())
        //$('#email').attr('value',email.trim())
        //$('#password').attr('value',password.trim())
        //$('#rpassword').attr('value',password.trim())

	$('#btnsave').click(function(){
                var username = $('#username').val().trim()
                var email = $('#email').val().trim()
                var password = $('#password').val().trim()
                var rpassword = $('#rpassword').val().trim()

                if (!checkuser(username))
                            return

                if (!checkemail(email))
                    return

                if (!checkpasswd(password))
                    return

                if (!checkrpasswd(rpassword))
                    return
		if ( password != rpassword ) {
                        $('#comparepasswd').html('The password and confirm password are different!')
                        return
                }
                else {
                        $('#comparepasswd').html('')
                }


                type = 'POST'
                url = '/users/edit/' + id
                data = {username:username,email:email,password:password,id:id}

                function successfn(data) {
                    location.reload()
                }

                function errorfn() {
                        $('#errorstatus').html('Sorry. The server has an exception!')
                }
                myajax(type,url,data,successfn,errorfn)

        })

        $('#username').change(function(){
                var username = $('#username').val().trim()
                console.log('username change')
        
                if (!checkuser(username))
            	    return
        
                type = 'POST'
                url = '/checkuser' 
                data = {username:username}
                
                function successfn1(data) {
            	    console.log('successfn111111')
            	    console.log(data)
            	    if (data['status'] == 1) {
                            $('#checkuserinfo').html('This user exist. Please change another username!')
            		  //  $('#btnsave').attr('disabled',true)
            		    return false
            	    }
            	    else {
            	    console.log('user no exist')
                        $('#checkuserinfo').html('')
        		console.log('enale disabled')
        		//$('#btnsave').attr('disabled',false)
            	    }
        
                }
                
                function errorfn1() {
            	    console.log('ajax error')
                        $('#errorstatus').html('Sorry. The server has an exception!')
                }
        
                myajax(type,url,data,successfn1,errorfn1)
        
        })
        
        $('#email').change(function(){
                var email = $('#email').val().trim()
                if (!checkemail(email))
            	    return
        
                type = 'POST'
                url = '/checkemail' 
                data = {email:email}
        
                function successfn2(data) {
            	    if (data['status'] == 1) {
            	            $('#checkemailinfo').html('This email exist. Please change another email!')
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
                }
        
                myajax(type,url,data,successfn2,errorfn2)
        
        
        })
        
        $('#password').change(function(){
                var password = $('#password').val().trim()
                if (!checkpasswd(password))
            	    return
        
        })
        
        $('#rpassword').change(function(){
                var password = $('#password').val().trim()
                var rpassword = $('#rpassword').val().trim()
                if (!checkrpasswd(rpassword))
            	    return
        
                if ( password != rpassword ) {
            	    $('#comparepasswd').html('The password and confirm password are different!')
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
    	            location.reload()

    	    }
    	    
    	    function errorfn4() {
    		    console.log('del ajax error')
    	    }

            myajax(type,url,data,successfn4, errorfn4)

    })
       
})

