var uncheck=(function(){
    function reset(e)
    {   console.log(e);
        if(this.checked==False)
        {
            this.checked==True;
        }
        else{
            this.checked==False;
        }
    }


   function init()
   {
    document.getElementById("choice_given_1_0").addEventListener('click', reset);
   }
    

    return{
        init:init;
    }
 })()