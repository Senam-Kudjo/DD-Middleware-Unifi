// shortcuts
function log(out){
  console.log(out)

}

let fieldset=document.getElementsByTagName("fieldset")
fieldset.item(0).style.width="50%"

let default_data_bundle=document.querySelector('label[for="id_Data_Bundle_0"]')
default_data_bundle.style.display="none"

let show_data_allocation=document.querySelector('input[id="id_show_custom_data_allocator"]')

let hide_data_allocation_label=document.querySelector('label[for="id_show_custom_data_allocator"]')
hide_data_allocation_label.style.display="none"

let Full_Name_Label=document.querySelector('label[for="id_Full_Name"]')
//Full_Name_label.innerHTML="Name"
let lineBreak = document.createElement('br');
Full_Name_Label.appendChild(lineBreak)


let Phone_Number_Label=document.querySelector('label[for="id_Phone_Number"]')
Phone_Number_Label.innerHTML="Phone No"

let getAmountfield=document.getElementById("id_Amount")

let disable_ID_Data_Bundle = document.querySelectorAll('input[type="radio"]');
let list_radioButtons=document.getElementById("id_Data_Bundle")
let length_of_radioButton=list_radioButtons.childElementCount



let align_radio_buttons=document.querySelectorAll('div[id="id_Data_Bundle"]')

align_radio_buttons.item(0).style.marginLeft="0%"
align_radio_buttons.item(0).style.padding="2%"
align_radio_buttons.item(0).style.textTransform="uppercase"




function data_allocation(pay){
  if (typeof(pay)=="number" | typeof(pay)=="string"){

    if (pay >0.0 & pay <=10){
          let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay >2 & pay <=10")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"


        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
    }
    else if (pay >10 & pay <=20){
        let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay >10 & pay <=20")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      


    }

    else if (pay >20 & pay <=50){
      let rate_deductions=(percent)=> percent/100;
      let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay >20 & pay <=50")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      


    }

    else if (pay>50 & pay<=100){
        let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay>50 & pay<=100")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      

    }

    else if (pay>100 & pay<=200){
        let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay>100 & pay<=200")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      

    }


    else if (pay>200 & pay<=300){
        let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay>200 & pay<=300")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      

    }

    else if (pay>300 & pay<=500){
        let rate_deductions=(percent)=> percent/100;
        let calc=(pay,percent)=>(pay/3 *340.29*rate_deductions(percent)*100).toFixed(2);
        let lengthOfValue=(calc(pay,1).length)
        if (lengthOfValue>6){
          log("pay>300 & pay<=500")
          show_data_allocation.value=Math.round((calc(pay,1)/1000).toFixed(2))+" "+"GB"

        }
        else{
          show_data_allocation.value=Math.round(calc(pay,1))+" "+"MB"
        }
      

    }
    else{
      
      show_data_allocation.value=""

    }

  }




}


function getvalueFromAmout(){

  if (getAmountfield.value.length>0){
      for (let x=1;x < length_of_radioButton;x++){
         disable_ID_Data_Bundle.item(x).disabled=true
      }

      typeof(getAmountfield.value)
      data_allocation(getAmountfield.value)



  }

  else{
      for (let x=1;x < length_of_radioButton;x++){
         disable_ID_Data_Bundle.item(x).disabled=false
         show_data_allocation.value=""
      }
  }


}



function getradiobuttons(){

  for (let x=1;x < length_of_radioButton;x++){
    if (disable_ID_Data_Bundle.item(x).checked==true){
      getAmountfield.readOnly=true
      getAmountfield.style.color = "#777";
      getAmountfield.style.backgroundColor = "#eee";
      getAmountfield.style.border = "1px solid #ccc";

    }
  

    getAmountfield.addEventListener(
      "click",function (){
        if (disable_ID_Data_Bundle.item(x).checked==true) {
          getAmountfield.readOnly=false 
          getAmountfield.style.color = "";
          getAmountfield.style.backgroundColor = "";
          getAmountfield.style.border = "";
          disable_ID_Data_Bundle.item(0).checked=true
        }
    
      }
    )
  }
}
