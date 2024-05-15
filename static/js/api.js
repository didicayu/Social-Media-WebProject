// JavaScript function to fetch trending posts from Twitter API and send them to Django backend
async function fetchAndSendPostsToBackend() {
    const response = await fetch('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=10');
    const data = await response.json();

    // Send the fetched data to Django backend using AJAX
    $.ajax({
        type: 'POST',
        url: '/save_twitter_posts/', // URL to your Django view to save Twitter posts
        data: JSON.stringify(data),
        contentType: 'application/json',
        success: function(response) {
            console.log('Twitter posts saved successfully:', response);
        },
        error: function(xhr, errmsg, err) {
            console.error('Error saving Twitter posts:', errmsg);
        }
    });
}
