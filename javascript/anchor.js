$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        var scrollToPosition = $(target).offset().top - 50;
        $('html').animate({ 'scrollTop': scrollToPosition }, 600);
        //$('html, body').animate({
        //  scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});
