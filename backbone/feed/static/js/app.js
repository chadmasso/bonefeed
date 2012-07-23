$(function(){

    var Post = Backbone.Model.extend({

        defaults: function() {
            return {
                text: "",
                comments: []
            };
        },

        clear: function() {
            this.destroy();
        },

        initialize: function(){
            //console.log(this.comment_set);
        },

        parse: function(response){
            this.comments = response.comments;
            var p = this;
            var comment_set = [];
            _.each(this.comments, function(obj){ var c = new Comment(obj); c.parent = p; comment_set.push(c); });
            this.comment_set = new CommentCollection(comment_set);
            return response;
        }

    });

    var PostCollection = Backbone.Collection.extend({

        urlRoot: '/api/v1/post/',

        model: Post

    });

    var Posts = new PostCollection;


    var PostView = Backbone.View.extend({

        tagName: 'div',

        template: _.template($('#post-template').html()),

        events: {
            "click .text":  "editText",
            "keypress .edit_text":  "saveText",
            "click .fetch":  "fetchModel"
        },

        initialize: function() {
            this.model.bind('change', this.render, this);
            this.model.bind('destroy', this.remove, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            this.addComments();
            this.edit_input = this.$('.edit_text');
            return this;
        },

        addComment: function(parentView, comment){
            var view = new CommentView({model: comment});
            console.log(parentView);
            this.$el.append(view.render().el);
        },

        addComments: function(){
            var parentView = this;
            this.model.comment_set.each(function(comment){parentView.addComment(parentView, comment);});
        },

        editText: function(){
            this.edit_input.show();
            this.edit_input.focus();
        },

        saveText: function(e){
            if (e.keyCode != 13) { return; }
            this.model.save({text: this.edit_input.val()});
            this.edit_input.hide();
        },

        fetchModel: function(){
            this.model.fetch();
        }

    });

    var Comment = Backbone.Model.extend({

        defaults: function() {
            return {
                text: ""
            };
        },

        clear: function() {
            this.destroy();
        },

        initialize: function(){
            //this.post_id =
            console.log(this);
        }

    });


    var CommentCollection = Backbone.Collection.extend({

        urlRoot: '/api/v1/comment/',

        model: Comment

    });

    var CommentView = Backbone.View.extend({

        tagName: 'div',

        template: _.template($('#comment-template').html()),

        /*
        events: {
            "click .text":  "editText",
            "keypress .edit_text":  "saveText",
            "click .fetch":  "fetchModel"
        },
        */
        initialize: function() {
            this.model.bind('change', this.render, this);
            this.model.bind('destroy', this.remove, this);
        },

        render: function() {
            this.$el.html(this.template(this.model.toJSON()));
            //this.edit_input = this.$('.edit_text');
            return this;
        },

        fetchModel: function(){
            this.model.fetch();
        }

    });

    var AppView = Backbone.View.extend({

        el: $("#content"),

        events: {
            "keypress #new_post":  "createOnEnter"
        },

        initialize: function() {
            this.new_post_input = this.$('#new_post');

            Posts.bind('add', this.addOne, this);
            Posts.bind('reset', this.addAll, this);
            Posts.bind('all', this.render, this);

            Posts.fetch();
        },

        render: function(){
            console.log("render in app");
        },

        addOne: function(post) {
            var view = new PostView({model: post});
            this.$('#feed').append(view.render().el);
        },

        addAll: function() {
            this.$('#feed').html("");
            Posts.each(this.addOne);
        },

        createOnEnter: function(e) {
            if (e.keyCode != 13) { return; }
            if (!this.new_post_input.val()){ return; }

            Posts.create({text: this.new_post_input.val()});
            this.new_post_input.val('');
        }

    });

    var App = new AppView;

$('#sync').click(function(){
    Posts.fetch();
});

});