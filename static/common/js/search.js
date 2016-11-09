var Search=(function(){

	function update(response){
		list=response.data;
		var i=0;
		if(list.length===0){
			$('.collection-header').html('No Results Found');}
		else{
			$('.collection-header').html(list.length+' Questions Found');
		}

		$('.collection-item').remove();
		for(i=0;i<list.length;i++)
		{  
			$('.collection').append('<li class="collection-item"><a href="/question/'+list[i].id+'/practice">'+list[i].question+"</a></li>");
		}
       
		
	}


	function perform_search(e){
		
		$.ajax({
			url:'/question/search',
			type:'GET',
			data:{'term':$('#id_search').val()},
			success:update,
			error:function(error){
				console.log(error);
			}
		})
	}

	function clear_all(e){
		console.log("clear")
		$('.collection-header').html('Type Something On the Top!!');
		$('.collection-item').remove();
		$('#id_search').val('')
	}


	function init(){

		$('#id_search').keyup(perform_search);
		$('#id_search').focusout(clear_all);

	}


	return {
		init:init
	};

})();