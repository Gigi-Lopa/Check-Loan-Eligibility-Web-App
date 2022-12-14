document.addEventListener("DOMContentLoaded", ()=>{
  document.querySelectorAll("td[id='loanAmount']").forEach(row =>{
   console.log(row)
    let loanamont = parseInt(row.textContent)
   $(row).empty()
   $(row).append((loanamont*1000))
  })
})
$("input[name='ApplicantIncome']").keyup(()=>{
    let applicantIncome = $("input[name='ApplicantIncome']").val()
    applicantIncome = parseInt(applicantIncome)
    if(applicantIncome < 50){
    $("#AIErrmsg").fadeIn(200,()=>{
        this.show           
    })
    document.querySelector("#AmIEligible").disabled = true;
    }
    else{
        $("#AIErrmsg").fadeOut(200,()=>{
            this.hide
        })
        document.querySelector("#AmIEligible").disabled = false;
    }
})
$(document).ready(function() {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });
$(document).on('click', '.nav-menu a, .scrollto', function(e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      e.preventDefault();
      var target = $(this.hash);
      if (target.length) {

        var scrollto = target.offset().top;

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
        }
        return false;
      }
    }
  });
  $(document).on('click', '.mobile-nav-toggle', function(e) {
    $('body').toggleClass('mobile-nav-active');
    $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
  });
  $(document).click(function(e) {
    var container = $(".mobile-nav-toggle");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
      if ($('body').hasClass('mobile-nav-active')) {
        $('body').removeClass('mobile-nav-active');
        $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      }
    }
  });

function validateFields(className, errsMsg){
    let field = $(className).val() 
    if(field == ""){
        $(errsMsg).fadeIn(200,()=>{
            this.show           
        })
        document.querySelector("#AmIEligible").disabled= true
        return false
    }  
    else{
        document.querySelector("#AmIEligible").disabled = false
        return true
    }
}
document.addEventListener("DOMContentLoaded",()=>{
    $("#AIErrmsg").hide()
    $("#AssetsErrmsg").hide()
    $("#coapplicant-income").hide()
    $("#loanAmountErr").hide()
    $("#paymentTermsErr").hide()
})
function validate(){
    let salary = validateFields("input[name='ApplicantIncome']", "#AIErrmsg")
    let coapplicantIncome = validateFields("input[name='CoapplicantAmount']", "#coapplicant-income")
    let loanAmount = validateFields("input[name='LoanAmount']","#loanAmountErr")
    let paymentTerms = validateFields("input[name='Payment_terms']","#paymentTermsErr")
    let assetVal = validateFields("input[name='assets']", "#AssetsErrmsg")
    if (salary && coapplicantIncome && loanAmount && paymentTerms && assetVal){
        return true
    }
    else{
        return false
    }
}
let forms =document.querySelector("form"); 
if (forms.length > 0){
    forms.addEventListener("submit",e=>{
        if(!validate()){
            e.preventDefault()
        }
     })
}
function loadScreen(data, loanAmount){
    let status_text = ""
    if (data === 'Y'){
        status_text = "Congradatulations You are Eligible for a loan"   
    }
    else if (data === 'N'){
        status_text = "Sorry, You are NOT Eligble for a loan"
        getPossibleLoanOffer(loanAmount)
    }
    document.querySelector(".text-content").querySelector("h1").innerHTML = status_text;   
    
  }
function getPossibleLoanOffer(loanAmount){
  let possibleLoanOffer = Math.round(( loanAmount - (0.4*loanAmount))*1000)
  document.querySelector(".text-content").querySelector("h2").innerHTML = `Possible loan Offer: ${possibleLoanOffer}`;   
}