$(function(){

    var Post = Backbone.Model.extend({
        url: '/post',
        defaults: function() {
            return {
                _id: 0,
                text: ""
            };
        },

        clear: function() {
            this.destroy();
        },

        parse: function(response) {
            return response;
        }

    });

    var PostCollection = Backbone.Collection.extend({

        url: '/posts',

        model: Post,

        parse: function(response) {
            console.log(response.posts);
            return response.posts;
        }

    });

    var Posts = new PostCollection;


    var PostView = Backbone.View.extend({

        tagName: 'div',

        template: _.template($('#post-template').html()),

        initialize: function() {
            this.model.bind('change', this.render, this);
            this.model.bind('destroy', this.remove, this);
        },

        render: function() {
            console.log(this.model.toJSON());
            this.$el.html(this.template(this.model.toJSON()));
            return this;
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

});