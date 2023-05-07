// 设置用户登录的显示

$('[datas-toggle="dropdown"]').on('click',function(event){
  event.preventDefault();
  $(this).siblings('.dropdown-menu').toggle();
})