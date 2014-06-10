var modal;
jQuery(document).ready(function(){
	

	jQuery('#vdsShare').live("click",function(event){
		event.preventDefault();
		var child=window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(location.href),'facebook-share-dialog','width=626,height=436');
		
		
		if(readCookie('ViralEmailOpt') === null) { 
			var timer=setInterval(checkChild, 500);
		}
		function checkChild() {
			if (child.closed) {
				clearInterval(timer);
				jQuery('.modalLink').trigger('click'); 
				
			}
			return false;
		}
		
		function readCookie(name) {
			  var nameEQ = name + "=";
			  var ca = document.cookie.split(';');
			  for(var i=0;i < ca.length;i++) {
				var c = ca[i];
				while (c.charAt(0)==' ') c = c.substring(1,c.length);
				if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
			  }
			  return null;
			}
			return false;
			
	});


    jQuery('.modalLink').modal({
        trigger: '.modalLink',          // id or class of link or button to trigger modal
        olay:'div.overlay',             // id or class of overlay
        modals:'div.modal',             // id or class of modal
        animationEffect: 'slideDown',   // overlay effect | slideDown or fadeIn | default=fadeIn
        animationSpeed: 400,            // speed of overlay in milliseconds | default=400
        moveModalSpeed: 'slow',         // speed of modal movement when window is resized | slow or fast | default=false
        background: '333333',           // hexidecimal color code - DONT USE #
        opacity: 0.7,                   // opacity of modal |  0 - 1 | default = 0.8
        openOnLoad: false,              // open modal on page load | true or false | default=false
        docClose: true,                 // click document to close | true or false | default=true    
        closeByEscape: true,            // close modal by escape key | true or false | default=true
        moveOnScroll: true,             // move modal when window is scrolled | true or false | default=false
        resizeWindow: true,             // move modal when window is resized | true or false | default=false
        video: 'http://player.vimeo.com/video/2355334?color=eb5a3d',    // enter the url of the video
        videoClass:'video',             // class of video element(s)
        close:'.closeBtn'               // id or class of close button
    });
	
	
	 	jQuery('#vdsNoMore').live('click', function() { 
  	
					jQuery('.closeBtn').trigger('click');
					//setting cookie
					var days=15;
					var date = new Date();
					date.setTime(date.getTime()+(days*24*60*60*1000));
					var expires = "; expires="+date.toGMTString();
					document.cookie = "ViralEmailOpt=1"+expires+"; path=/";
					return false;
        	});
			
			
			
});
