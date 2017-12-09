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


function check(){

        var username = $('#username').val().trim()
        var email = $('#email').val().trim()
        var password = $('#password').val().trim()
        var rpassword = $('#rpassword').val().trim()

        if (!checkuser(username))
                return false

        if (!checkemail(email))
                return false

        if (!checkpasswd(password))
                return false

        if (!checkrpasswd(rpassword))
                return false
	if ( password != rpassword ) {
               $('#comparepasswd').html('The password and confirm password are different!')
               return
        }
	else {
               $('#comparepasswd').html('')
        }


        return true


}

$('#username').change(function(){
        var username = $('#username').val().trim()

        if (!checkuser(username))
                return false 

        type = 'POST'
        url = '/checkuser'
        data = {username:username}

        function successfn1(data) {
               if (data['status'] == 1) {
                   $('#checkuserinfo').html('This user exist. Please change another username!')
                       $('#submit').attr("disabled","true")
                       return false
               }
               else {
                   $('#checkuserinfo').html('')
                   $('#submit').attr("disabled","false")
               }

       }

       function errorfn1() {
               $('#errorstatus').html('Sorry. The server has an exception!')
       }

        myajax(type,url,data,successfn1,errorfn1)

 })

$('#email').change(function(){
        var email = $('#email').val().trim()
        if (!checkemail(email))
                return false

        type = 'POST'
        url = '/checkemail'
        data = {email:email}
        function successfn2(data) {
                if (data['status'] == 1) {
                       $('#checkemailinfo').html('This email exist. Please change another email!')
                      // $('#submit').attr("disabled","true")
                       return false
               }
               else {
                   $('#checkemailinfo').html('')
                  // $('#submit').attr("disabled","false")
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
                return false

})

$('#rpassword').change(function(){
        var password = $('#submit_form_password').val().trim()
        var rpassword = $('#rpassword').val()
        if (!checkrpasswd(rpassword))
                return false

        if ( password != rpassword ) {
                $('#comparepasswd').html('The password and confirm password are different!')
                return false
        }
        else {
                $('#comparepasswd').html('')
        }


})

