(function(){
	
  // Look for .hamburger
  $(".button-collapse").css({"position":"absolute"})

  var hamburger = document.querySelector(".hamburger");
  var right=300;
  // On click
  hamburger.addEventListener("click", function() {
    // Toggle class "is-active"
    hamburger.classList.toggle("is-active");
    $("#nav").fadeToggle("slow");;
    $(".menu").animate({
        right: right+'px',
        
    },function(){
    	if(right===300)
    	{
    		right=20;
    	}
    	else{
    		right=300;
    	}
    });


    // Do something else, like open/close menu
  });


  $('canvas').css({'height':'80%'})
  var val;
   val=setInterval(trigger,2000);

  function trigger(){
    var random=Math.floor((Math.random() *4) + 1);
  var i=1;
  while(i<=4){
    
    $(".cs"+String(i)).hide();

    i++;
  }
  $(".cs"+String(random)).show();
  
  }


  $(".button-next").click(function(){
  
  var random=Math.floor((Math.random() *4) + 1);
  var i=1;
  while(i<=4){
  	
  	$(".cs"+String(i)).hide();
  	i++;
  }
  



  $(".cs"+String(random)).show();
  });

  $(".button-prev").click(function(){
  
  var random=Math.floor((Math.random() *4) + 1);
  var i=1;
  while(i<=4){
  	$(".cs"+String(i)).hide();
  	i++;
  }
  

  $(".cs"+String(random)).show();
  });

})();