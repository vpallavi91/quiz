var action;
var check=(function(){
  var setCheck;
    function radio(e){
    if(setCheck != this){
             setCheck = this;
        }
        else{
            this.checked = false;
            setCheck = null;
    }
    };
    function handlecheck(e) {
     e.preventDefault();
     data = new FormData($('form')[0]);
     $.ajax({
       url:action,
      type:"POST",
      data: data,
       processData: false,
       dataType: 'json',
       contentType: false,
       success: function(response, xhr) {
         correct=response.correct;
         rad_list=$("[id=id_choices_given]")
         	for(var x=0;x<rad_list.length;x++)
         	{
         		if(rad_list[x].children[1].innerHTML==correct)
         		{
         			rad_list[x].style.backgroundColor="#7986cb";
         		}
         		else{
         			if(rad_list[x].children[0].checked==true)
         				rad_list[x].style.backgroundColor="#ef9a9a"
         		}
         	}

         
         
         myrads=$('form')[0].getElementsByClassName('radio');
         for(var k=0;k<myrads.length;k++)
          myrads[k].children[0].disabled=true;
         $("#login-btn").hide();
         $("#pin").show();

       },
       error: function(error) {
         console.log(error);
      }
     });
   }
   function init(act)
   {action=act;
    var myRadios =document.getElementsByClassName("with-gap")
    var setCheck;
    var x = 0;
    for(x = 0; x < myRadios.length; x++){

    myRadios[x].onclick =radio;


}
    $('#login-btn').click(handlecheck);


   }
    

    return{
        init:init,
    }})();
