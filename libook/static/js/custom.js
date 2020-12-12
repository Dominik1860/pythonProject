// const baseUrl = 'http://127.0.0.1:8000';
const baseUrl = 'https://li-book.herokuapp.com';

function handleAddToFriendsClick(elem) {
    var friendId = elem.getAttribute("data-friend-id");
    var endpoint = `${baseUrl}/profile/addfriend/?friend_id=${friendId}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false);
    xmlHttp.send();
    // alert("You have added a new friend.");
    location.reload();
}

function handleRemoveFromFriendsClick(elem) {
    var friendId = elem.getAttribute("data-friend-id");
    var endpoint = `${baseUrl}/profile/removefriend/?friend_id=${friendId}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false);
    xmlHttp.send();
    // alert("You have removed this friend.");
    location.reload();
}

function handleEventSignupButtonClick(elem) {
    var eventId = elem.getAttribute("data-event-id");
    var endpoint = `${baseUrl}/events/signup/?event_id=${eventId}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false); // false => asynchronous request
    xmlHttp.send(null);
    // alert("You have successfully signed up.");
    location.reload();
}

function handleEventUnsubscribeButtonClick(elem) {
    var eventId = elem.getAttribute("data-event-id");
    var endpoint = `${baseUrl}/events/unsubscribe/?event_id=${eventId}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false); // false => asynchronous request
    xmlHttp.send(null);
    // alert("You have successfully unsubscribed.");
    location.reload();
}

function handleCommentClick(elem) {
    var postId = elem.getAttribute("data-post-id");
    var userId = elem.getAttribute("data-user-id");
    var content = prompt("Write down your comment:");
    var endpoint = `${baseUrl}/posts/comment/create/?post_id=${postId}&user_id=${userId}&content=${content}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false); // false => asynchronous request
    xmlHttp.send(null);
    location.replace(`${baseUrl}/posts/detail/${postId}`);
}

function handleLikeClick(elem) {
    var postId = elem.getAttribute("data-post-id");
    var endpoint = `${baseUrl}/posts/like/create/?post_id=${postId}`;
    var xmlHttp = new XMLHttpRequest();

    xmlHttp.open("GET", endpoint, false); // false => asynchronous request
    xmlHttp.send(null);
    // alert("You successfully liked the post.");
    location.reload();
}

