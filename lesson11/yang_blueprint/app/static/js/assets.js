//验证表单
$("#addform").validate();
// 添加资产
$("#btn_addsave").click(function(){
   
   if (!$("#add_form").valid() ) {
       return ;
   } else {
        var retdata = $("#add_form").serialize();
        $.post("/assets", retdata, function(response){
            $("#add_asset_modal").modal('hide');
            console.log(response.status);
               if ( response.status == 0 ) {
                   swal({
                     title: "添加资产完成！",
                     type: "info",
                     showCancelButton: true,
                     closeOnConfirm: false,
                     showLoaderOnConfirm: true,
                   },
                   function(){
                         setTimeout(function(){
                             swal(response.message);
                         }, 2000);
                         location.reload();
                   });
               } else {
                   swal(response.message, '', "error")
               };
        });
   }
        });

// 删除资产
$(".del_asset").click(function() {
    //var pk= $(this).attr('pk')
    id = $(this).attr('uid');
    $.get('/assets/del/', { 'id' : id }, function() {
        swal("干得漂亮！", "删除记录成功！","success")
    });
});

// 修改资产
$(".edit_asset").click(function() {
    console.log('hahahhah')
    id = $(this).attr('uid');
    var hostname = $(this).parents("tr").children("td").eq(1).text()
    var host_status= $(this).parents("tr").children("td").eq(2).text()
    var private_ip= $(this).parents("tr").children("td").eq(3).text()
    var public_ip = $(this).parents("tr").children("td").eq(4).text()
    var mem_total = $(this).parents("tr").children("td").eq(5).text()
    var disk = $(this).parents("tr").children("td").eq(6).text()
    var cpu_num = $(this).parents("tr").children("td").eq(7).text()
    var cpu_model = $(this).parents("tr").children("td").eq(8).text()
    var machine_room = $(this).parents("tr").children("td").eq(9).text()
    $('#edit_asset_modal').modal('show')

    $('#edit_hostname').attr('value',hostname.trim())
    $('#edit_private_ip').attr('value',private_ip.trim())
    $('#edit_public_ip').attr('value',public_ip.trim())
    $('#edit_mem_total').attr('value',mem_total.trim())
    $('#edit_disk').attr('value',disk.trim())
    $('#edit_cpu_num').attr('value',cpu_num.trim())
    $('#edit_cpu_model').attr('value',cpu_model.trim())
    $('#edit_machine_room').attr('value',machine_room.trim())
   $("#btn_editsave").click(function(){ 
    var hostname = $('#edit_hostname').val()
    var private_ip= $('#edit_private_ip').val()
    var public_ip = $('#edit_public_ip').val()
    var mem_total = $('#edit_mem_total').val()
    var disk = $('#edit_disk').val()
    var cpu_num =$('#edit_cpu_num').val()
    var cpu_model = $('#edit_cpu_model').val()
    var machine_room = $('#edit_machine_room').val()
    
    data = {"id":id,"hostname":hostname,"private_ip":private_ip,"public_ip":public_ip,"mem_total":mem_total,"disk":disk,"cpu_num":cpu_num,"cpu_model":cpu_model,"machine_room":machine_room}
    console.log(machine_room)
    $.post("/assets/edit",data,function(data){
    //$('#edit_asset_modal').modal('hide')
       location.reload();
    });

   });

});

// 查看资产详情
$(".info_asset").click(function() {
    alert('info asset');
});

