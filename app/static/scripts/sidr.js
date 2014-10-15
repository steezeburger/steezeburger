/**
 * Created by js on 10/15/14.
 */
$(document).ready(function() {
   $('#glitch-menu').sidr({
       name: 'glitch',
       side: 'right',
       source: '#glitch-menu-content'
   });
   $('#projects-menu').sidr({
       name: 'projects',
       side: 'right',
       source: '#projects-menu-content'
   });
   $('#mobile-menu').sidr({
       name: 'mobile',
       side: 'right',
       source: '#mobile-menu-content'
   });
//   .bind('click', function (){
//       $.sidr('close', 'sidr-main');
//   });
//   .bind('touchstart', function(){
//       $.sidr('close', 'sidr-main');
//   });
});

//$(document)
//    .bind('click', function (){
//        $.sidr('close', 'sidr-main');
//    })
//    .bind('touchstart', function(){
//        $.sidr('close', 'sidr-main');
//    });