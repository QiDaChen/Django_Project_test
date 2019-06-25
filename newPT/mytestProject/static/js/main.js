$(function(){
	
	$('.index_top ul:first li').mouseover(function(){
		$(this).addClass('hhover')
	}).mouseout(function(){
		$(this).removeClass('hhover')
	});
	$('.index_mian_demo').slideDown('slow');
	$('.zhuce').click(function(){
//		alert('应该执行了')
		$(".zcb").show()
		return false;
	});
	$('form>input').focus(function(){
		$(this).addClass('jiacu')
	}).focusout(function(){
		$(this).removeClass('jiacu')
	})
	$('#exit').click(function(){
		$('.zcb').hide()
		return false;
		
	});
	$('#submit').click(function(){
		alert('此功能尚未完成。。。');
	})
	$('#exit,#submit,input').mouseover(function(){
		$(this).addClass('active')
	}).mouseleave(function(){
		$(this).removeClass('active')
	});
	$('.scrn').draggable({
		containment:'parent',
		axis:'x',
		opacity:0.5,
		drag:function(ev,ui){
			var nowleft = ui.position.left;
			var ple = $(this).parent('.bar').parent('li').prev('li').prev('li').children('h2');
			if(nowleft>0 && nowleft<=100){
				ple.text('入门');
			}
			else{
				if (nowleft>100 && nowleft<=200) {
					ple.text('熟悉');
				} else{
					if (nowleft>200 && nowleft<=300) {
					ple.text('掌握');
				} else{
					if (nowleft>300 && nowleft<=400) {
					ple.text('精通');
				} 
				}
				}
			}
//			console.log()
//			alert(nowleft)
			console.log(nowleft)
		}
	})
	
})