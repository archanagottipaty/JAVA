
$(document).ready(function () {

  console.log(parseInt(moment().format('H')))

  const currentTime = moment().format('Do YYYY MMMM')
  $("#currentTime").text(currentTime)
  $("span").attr("style", "width: 75px")
  $("span").attr("style", "width: 75px")

 $("button").css("color", "red")
 //$("button").css("fill", "green")
//  $(".col-sm-12").css("padding-left",0)
 // $(".row").css("height",54);
  // $("body").attr("height","100%")
  // background-image: url("img_girl.jpg");
  // $("body").attr("background-image", "bg.jpg")
  // $("body").attr("background-size","cover")
  $(".bg").css("background-image", "url('bg.jpg')");
  $('span').css("font-family",'Syne Tactile');

  // background-size: cover;



  const times = [9, 10, 11,12,13,14,15,16,17]

  times.forEach(time => {
    const timeCheck = JSON.stringify(window.localStorage.getItem(time))
    const currentHour = moment().hour()
    const timeId = "#" + time

    if (currentHour > time) {
      $(timeId).addClass("bg-danger text-light")
      $(timeId).attr("disabled", true)
    } else if (currentHour === time) {
      $(timeId).addClass("bg-secondary text-light")
    } else {
      $(timeId).addClass("bg-success text-light")
    }

    if (timeCheck === null) window.localStorage.setItem(time, "");
    //console.log("timeCHeck.lenght()" +timeCheck.length);
    if (timeCheck.length > 0) $(timeId).attr("value", window.localStorage.getItem(time));
  });
 
  

  $("form").on("submit", function (e) {
    e.preventDefault()
    //$("span").animate({left: '250px'});
    //$("i").animate({color:'black'},100);

    const time = e.target.querySelector("input").getAttribute("id")
    const text = e.target.querySelector("input").value

    window.localStorage.setItem(time, text)
  });
});
