

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all components
    const app = new NewsDetailApp();
    app.initialize();
});

class NewsDetailApp {
    constructor() {
        // Core configuration
        this.postId = '{{ object.id }}';
        this.currentUserId = '{{ user.id }}';
        this.currentUsername = '{{ user.username }}';
        this.csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

        // UI components
        this.commentForm = document.getElementById('comment-form');
        this.commentsSection = document.getElementById('comments-section');
        this.showMoreBtn = document.getElementById('show-more-btn');

        // State
        this.allCommentsLoaded = false;
    }

    /**
     * Initialize all functionality
     */
    initialize() {
        // Initialize star rating system
        this.starRating = new StarRating(this.postId, this.csrfToken);

        // Initialize comment handlers for existing comments
        this.initializeComments();

        // Set up event listeners
        this.setupEventListeners();

        // Display user's previous votes and ratings if available
        this.loadUserInteractions();
    }

    /**
     * Initialize comment handlers for all comments
     */
    initializeComments() {
        document.querySelectorAll('.comment').forEach(commentElement => {
            new CommentHandler(commentElement, this.csrfToken, this.currentUserId);
        });
    }

    /**
     * Set up all event listeners
     */
    setupEventListeners() {
        // Comment form submission
        if (this.commentForm) {
            this.commentForm.addEventListener('submit', this.handleCommentSubmission.bind(this));
        }

        // Show more comments button
        if (this.showMoreBtn) {
            this.showMoreBtn.addEventListener('click', this.loadMoreComments.bind(this));
        }

        // Reply buttons
        document.querySelectorAll('.reply-button').forEach(button => {
            button.addEventListener('click', this.handleReplyClick.bind(this));
        });
    }

    /**
     * Load user's previous interactions (votes, ratings)
     */
    loadUserInteractions() {
        // Fetch user's previous ratings and votes if they're logged in
        if (this.currentUserId && this.currentUserId !== 'None') {
            this.fetchUserRating();
            this.fetchUserVotes();
        }
    }

    /**
     * Fetch user's previous rating for this post
     */
    async fetchUserRating() {
        try {
            const response = await fetch(`/api/ratings/?post_id=${this.postId}&user_id=${this.currentUserId}`);
            if (response.ok) {
                const data = await response.json();
                if (data.rating) {
                    this.starRating.setRating(data.rating);
                }
            }
        } catch (error) {
            console.error('Error fetching user rating:', error);
        }
    }

  /**
 * Fetch user's previous votes on comments
 */
async fetchUserVotes() {
    try {
        const response = await fetch(/api/votes/?post_id=${this.postId}&user_id=${this.currentUserId});

        // Check if the response is OK
        if (response.ok) {
            const data = await response.json();
            data.votes.forEach(vote => {
                // Corrected the selector syntax
                const commentEl = document.querySelector(.comment[data-comment-id="${vote.comment_id}"]);
                if (commentEl) {
                    const handler = new CommentHandler(commentEl, this.csrfToken, this.currentUserId);
                    handler.updateVoteDisplay(vote.likes, vote.dislikes, vote.user_vote);
                }
            });
        } else {
            console.error('Failed to fetch user votes:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Error fetching user votes:', error);
    }
}


    /**
     * Handle comment form submission
     * @param {Event} e - Form submission event
     */
    handleCommentSubmission(e) {
        e.preventDefault();
        this.showSnackbar();

        // Submit the form after a delay
        setTimeout(() => {
            this.commentForm.submit();
        }, 1000);
    }

    /**
     * Load more comments when "Show More" button is clicked
     */
    loadMoreComments() {
        const moreComments = document.getElementById('more-comments');
        if (moreComments) {
            moreComments.style.display = 'block';
            this.showMoreBtn.style.display = 'none';
            this.allCommentsLoaded = true;

            // Initialize handlers for newly displayed comments
            moreComments.querySelectorAll('.comment').forEach(commentElement => {
                new CommentHandler(commentElement, this.csrfToken, this.currentUserId);
            });
        }
    }

    /**
     * Handle reply button click
     * @param {Event} e - Click event
     */
    handleReplyClick(e) {
        const commentId = e.target.dataset.commentId;
        // Implement reply functionality here
        console.log(`Reply to comment ${commentId}`);

        // Example: scroll to comment form and add @username reference
        const commentAuthor = e.target.closest('.comment').querySelector('.comment-author').textContent;
        const commentContent = document.querySelector('textarea[name="content"]');
        if (commentContent) {
            commentContent.value = `@${commentAuthor.trim()} `;
            commentContent.focus();

            // Scroll to comment form
            this.commentForm.scrollIntoView({ behavior: 'smooth' });
        }
    }

    /**
     * Show snackbar notification
     * @param {string} message - Optional custom message
     */
    showSnackbar(message) {
        const snackbar = document.getElementById("snackbar");
        if (!snackbar) {
            console.error("Snackbar element not found");
            return;
        }

        if (message) {
            snackbar.textContent = message;
        }

        snackbar.classList.add("show");
        setTimeout(() => {
            snackbar.classList.remove("show");
        }, 3000);
    }
}

/**
 * Class for handling star rating functionality
 */
class StarRating {
    /**
     * Constructor
     * @param {string} postId - ID of the current post
     * @param {string} csrfToken - CSRF token for API requests
     */
    constructor(postId, csrfToken) {
        this.postId = postId;
        this.csrfToken = csrfToken;
        this.stars = document.querySelectorAll('.star-rating .star');
        this.ratingOutput = document.getElementById('rating-output');
        this.currentRating = 0;

        this.initialize();
    }

    /**
     * Initialize star rating system
     */
    initialize() {
        this.attachEventListeners();
    }

    /**
     * Attach event listeners to stars
     */
    attachEventListeners() {
        this.stars.forEach(star => {
            // Click event - set rating
            star.addEventListener('click', () => {
                const value = parseInt(star.dataset.value);
                this.setRating(value);
                this.submitRating(value);
            });

            // Hover events - preview rating

            star.addEventListener('mouseout', () => {
                this.resetStars();
                this.highlightRating(this.currentRating);
            });
        });
    }

    /**
     * Set the current rating
     * @param {number} rating - Rating value (1-5)
     */
    setRating(rating) {
        this.currentRating = rating;
        this.highlightRating(rating);
        this.updateRatingText(rating);
    }

    /**
     * Preview rating on hover
     * @param {number} rating - Rating value (1-5)
     */
    previewRating(rating) {
        this.resetStars();
        this.highlightRating(rating);
        this.updateRatingText(rating);
    }

    /**
     * Reset stars to default state
     */
    resetStars() {
        this.stars.forEach(star => {
            star.classList.remove('active');
        });
    }

    /**
     * Highlight stars based on rating
     * @param {number} rating - Rating value (1-5)
     */
    highlightRating(rating) {
        this.stars.forEach(star => {
            const value = parseInt(star.dataset.value);
            if (value <= rating) {
                star.classList.add('active');
            }
        });
    }

    /**
     * Update rating text display
     * @param {number} rating - Rating value (1-5)
     */
    updateRatingText(rating) {
        if (this.ratingOutput) {
            this.ratingOutput.textContent = `Rating: ${rating}/5`;
        }
    }

    /**
     * Submit rating to server
     * @param {number} rating - Rating value (1-5)
     */
    async submitRating(rating) {
        try {
            const response = await fetch('/rate/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrfToken
                },
                body: JSON.stringify({
                    post_id: this.postId,
                    rating: rating
                })
            });

            if (!response.ok) {
                throw new Error('Failed to submit rating');
            }

            const result = await response.json();
            if (result.success) {
                console.log('Rating submitted successfully');
            }
        } catch (error) {
            console.error('Error submitting rating:', error);
        }
    }
}

/**
 * Class for handling comment like/dislike functionality
 */
class CommentHandler {
    /**
     * Constructor
     * @param {HTMLElement} commentElement - Comment DOM element
     * @param {string} csrfToken - CSRF token for API requests
     * @param {string} userId - Current user ID
     */
    constructor(commentElement, csrfToken, userId) {
        this.commentElement = commentElement;
        this.commentId = commentElement.dataset.commentId;
        this.csrfToken = csrfToken;
        this.userId = userId;

        // UI elements
        this.likeBtn = commentElement.querySelector('.like-btn');
        this.dislikeBtn = commentElement.querySelector('.dislike-btn');
        this.likeCount = commentElement.querySelector('.like-count');
        this.dislikeCount = commentElement.querySelector('.dislike-count');

        // State
        this.userVote = null;

        this.initialize();
    }

    /**
     * Initialize comment handler
     */
    initialize() {
        this.loadInitialCounts();
        this.attachEventListeners();
    }

    /**
     * Load initial like/dislike counts
     */
    loadInitialCounts() {
        this.likeCount.textContent = this.likeCount.textContent || '0';
        this.dislikeCount.textContent = this.dislikeCount.textContent || '0';
    }

    /**
     * Attach event listeners to like/dislike buttons
     */
    attachEventListeners() {
        if (!this.userId || this.userId === 'None') {
            // If user is not logged in, add tooltip and return
            this.likeBtn.title = 'Please log in to like comments';
            this.dislikeBtn.title = 'Please log in to dislike comments';
            return;
        }

        this.likeBtn.addEventListener('click', () => this.handleVote('like'));
        this.dislikeBtn.addEventListener('click', () => this.handleVote('dislike'));
    }

    /**
     * Handle vote action (like/dislike)
     * @param {string} voteType - Type of vote ('like' or 'dislike')
     */
    async handleVote(voteType) {
        try {
            const response = await fetch('/vote/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.csrfToken
                },
                body: JSON.stringify({
                    comment_id: this.commentId,
                    vote_type: voteType,
                    user_id: this.userId
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            if (result.success) {
                this.updateVoteDisplay(result.likes, result.dislikes, result.user_vote);
            }
        } catch (error) {
            console.error('Error processing vote:', error);
        }
    }

    /**
     * Update vote display after vote action
     * @param {number} likes - New like count
     * @param {number} dislikes - New dislike count
     * @param {string} userVote - User's current vote ('like', 'dislike', or null)
     */
    updateVoteDisplay(likes, dislikes, userVote) {
        // Update counts
        this.likeCount.textContent = likes;
        this.dislikeCount.textContent = dislikes;

        // Update visual state
        this.likeBtn.classList.remove('liked');
        this.dislikeBtn.classList.remove('disliked');

        if (userVote === 'like') {
            this.likeBtn.classList.add('liked');
        } else if (userVote === 'dislike') {
            this.dislikeBtn.classList.add('disliked');
        }

        // Update stored state
        this.userVote = userVote;
    }
}

    function setMood(mood) {
  var a = document.getElementById("div1");
  switch(mood) {
    case 'happy':
      a.innerHTML = "&#xf118;"; // happy
      break;
    case 'sad':
      a.innerHTML = "&#xf119;"; // Sad
      break;
    case 'normal':
      a.innerHTML = "&#xf11a;"; // Normal
      break;

  }
}