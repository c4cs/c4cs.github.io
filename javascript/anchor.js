$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        var scrollToPosition = $(target).offset().top;
        $('html').animate({ 'scrollTop': scrollToPosition }, 60);
        //$('html, body').animate({
         // scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});
