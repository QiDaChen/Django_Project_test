$(function(){
	$('.daohanglan li').click(function(){
//		alert('fsjkfjs')
		$(this).siblings('li').removeClass('active');
		$(this).addClass('active');
	});
	$('.lever1').children('h2').css({ "color": "white"});
	$(".advts").animate({height: 40},2000);
	
});
