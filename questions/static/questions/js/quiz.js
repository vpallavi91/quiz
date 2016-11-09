var action;
var uncheck=(function(){
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
         result=response.result;
         label_list=response.label_list;
         var t="[id=id_choices_given_"
         var u="]";
         for(var i=0;i<label_list.length;i++)
         {
         	var j=i+1;
         	var c=t+j+u;
         	rad_list=$(c);
         	for(var x=0;x<rad_list.length;x++)
         	{
         		if(rad_list[x].children[1].innerHTML==label_list[i])
         		{
         			rad_list[x].style.backgroundColor="#7986cb";
         		}
         		else{
         			if(rad_list[x].children[0].checked==true)
         				rad_list[x].style.backgroundColor="#ef9a9a"
         		}
         	}

         }
        var txt="<div class='row green lighten-3'><div class='col s12'><h4>Congrats !!!</h4><h5>You Score is ";
        txt=txt+result;
        txt=txt+"</h5></div></div>";
        $(txt).insertBefore("#beforeit");
         
         myrads=$('form')[0].getElementsByClassName('radio');
         for(var k=0;k<myrads.length;k++)
          myrads[k].children[0].disabled=true;
         $("#login-btn").innerHTML="TRY MORE";
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
