const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// Message Alert Disappear Start
setTimeout(function () {

    $('#message').fadeOut('slow');
    
}, 3000);   // after 3 seconds it will disappear
// Message Alert Disappear End
// After this need to run python manage.py collectstatic