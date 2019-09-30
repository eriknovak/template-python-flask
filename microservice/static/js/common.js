$(document).ready(function () {
    // add function to all clickable rows
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});