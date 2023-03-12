

(function() {
  $(".form-group .form-field").on("focus change", function() {
    if (!($(this).closest(".form-group").hasClass("select") && $(this).val() === "")) {
      $(this).closest(".form-group").addClass("moved");
    }
  }).on("blur change", function() {
    if ($(this).val().trim() === "") {
      $(this).closest(".form-group").removeClass("moved");
    }
  }).on("change keypress", function() {
    $(this).closest(".invalid").removeClass("invalid");
  });

  window.emailRegex = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;

 

  $("form .error-message").on("click", function() {
    $(this).closest(".invalid").removeClass("invalid");
  });

  $(".bg-toggle").on("click", function() {
    $('body,form').toggleClass('dark');
  });

  if (!(/Mobi/.test(navigator.userAgent))) {
    $(".form-group.select select").on("mousedown touchstart focus", function(e) {
      var isOpen;
      e.preventDefault();
      isOpen = $(this).siblings(".dropdown").hasClass("open");
      $(".form-group .dropdown").removeClass("open");
      if (isOpen !== true) {
        $(this).siblings(".dropdown").addClass("open");
      }
      $(this).blur().siblings(".dropdown").find("a.selected").focus();
    }).each(function() {
      var dropdown, options;
      options = $(this).find("option");
      dropdown = $("<ul></ul>").addClass("dropdown");
      options.each(function() {
        var li, option, optionText, optionValue;
        optionValue = $(this).attr("value");
        optionText = $(this).text();
        li = $("<li></li>");
        option = $("<a></a>").attr({
          "href": "#",
          "data-val": optionValue
        }).text(optionText);
        if ($(this).attr("selected")) {
          option.addClass("selected");
        }
        option.on("click", function(e) {
          e.preventDefault();
          dropdown.find(".selected").removeClass("selected");
          $(this).addClass("selected").closest(".form-group").find("select").val($(this).attr("data-val")).trigger("change");
          dropdown.removeClass("open");
        }).on("keydown", function(e) {
          var key;
          key = e.keyCode ? e.keyCode : e.which;
          if (key === 40) {
            $(this).closest("li").next("li").find("a").focus();
          } else if (key === 38) {
            $(this).closest("li").prev("li").find("a").focus();
          }
        });
        li.append(option);
        return dropdown.append(li);
      });
      $(this).closest(".form-group").append(dropdown);
    });
  }

  $(document).on("click", function(e) {
    if (!$(e.target).closest(".form-group.select").find(".dropdown.open").length) {
      return $(".form-group .dropdown").removeClass("open");
    }
  });

}).call(this);









$(document).ready(function() {
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  let interval = null;

  document.querySelector("h1").onmouseover = event => {  
    let iteration = 0;
    
    clearInterval(interval);
    
    interval = setInterval(() => {
      event.target.innerText = event.target.innerText
        .split("")
        .map((letter, index) => {
          if(index < iteration) {
            return event.target.dataset.value[index];
          }
        
          return letters[Math.floor(Math.random() * 26)]
        })
        .join("");
      
      if(iteration >= event.target.dataset.value.length){ 
        clearInterval(interval);
      }
      
      iteration += 1 / 3;
    }, 20);
  }


  // Set up the alphabet and the character index
  var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  var charIndex = 0;

  // When the mouse is moved, update the position of the cursor
  $(document).on('mousemove', function(e){
    $('.cursor2').css({
      left: e.clientX + "px", 
      top: (e.clientY-15) + "px"
   
    });
  });

  // When the mouse is pressed, add the "hacking" class to the cursor
  $(document).on('mousedown', function(){
    $('.cursor').addClass('hacking');
  });

  $(document).on('mouseup', function(){
    // When the mouse is released, remove the "hacking" class from the cursor
    $('.cursor').removeClass('hacking');
  });

  setInterval(function() {
    // Update the cursor text with the next character in the alphabet
    var nextChar = alphabet[charIndex];
    $('.cursor-text').text(nextChar);
    
    // Increment the character index, wrapping around to 0 when it reaches the end of the alphabet
    charIndex = (charIndex + 1) % alphabet.length;
  }, 50);
});

