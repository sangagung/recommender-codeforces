$(document).ready(function(data) {
    $.get('http://codeforces.com/api/user.status?handle=ZakyKh', function(data) {
        alert(data)
    });
});