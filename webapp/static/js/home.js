
/*
{"recipe_name": "Cake", "ingredients": ["Bun", "Pattie"], "instructions": "Heat it !", "Serving Size": 2,
"category": "vegan", "notes": "trying to do "}
*/


$( document ).ready(function() {


var button = document.getElementById("add_ingredient_submit");




$("#add_ingredient_submit").click(function(){
    ingredient_name = $("#ingredient_name").val()
    $("#ingredient_list_div ul").append('<li class="list-group-item">'+ingredient_name+'</li>');

});

$("#edit_ingredient_submit").click(function(){
    ingredient_name = $("#edit_ingredient_name").val()
    $("#edit_ingredient_list_div ul").append('<li class="list-group-item">'+ingredient_name+'</li>');

});


$("#recipe_add_submit").click(function(){

    recipe_name = $("#recipe_name").val()
    category = $("#category").val()
    serving_size = parseInt($("#serving_size").val())
    ingredient_list = [];

    $('#ingredient_list li').each(function(i)
        {
            ingredient_list.push($(this).text());

        });
        console.log(ingredient_list);

    instructions = $('textarea#instructions').val();
    notes = $('textarea#notes').val();
    console.log(instructions);
    console.log(notes);

    console.log({"recipe_name": recipe_name, "category": category, "serving_size": serving_size,
                        "ingredients": "ingredient_list", "instructions": instructions, "notes": notes});

    console.log(recipe_name);
    console.log('/api/v1/recipe/'+recipe_name);

    $.ajax({
        type: 'POST',
        url: '/api/v1/recipe/'+recipe_name,
        data: JSON.stringify({"recipe_name": recipe_name, "category": category, "serving_size": serving_size,
                        "ingredients": ingredient_list, "instructions": instructions, "notes": notes}),
        success: function(data) {
            console.log('data: ' + data);
//            location.reload(true);
            window.location.replace("/");
             },
        contentType: "application/json",
        dataType: 'json'
    });

})


$("#recipe_edit_submit").click(function(){

    recipe_name = $("#edit_recipe_name").val()
    category = $("#edit_category").val()
    serving_size = parseInt($("#edit_serving_size").val())
    ingredient_list = [];

    $('#edit_ingredient_list li').each(function(i)
        {
            ingredient_list.push($(this).text());

        });
        console.log(ingredient_list);

    instructions = $('textarea#edit_instructions').val();
    notes = $('textarea#edit_notes').val();
    console.log(instructions);
    console.log(notes);

    console.log({"recipe_name": recipe_name, "category": category, "serving_size": serving_size,
                        "ingredients": "ingredient_list", "instructions": instructions, "notes": notes});



    $.ajax({
        type: 'PUT',
        url: '/api/v1/recipe/'+recipe_name,
        data: JSON.stringify({"category": category, "serving_size": serving_size,
                        "ingredients": ingredient_list, "instructions": instructions, "notes": notes}),
        success: function(data) {
            console.log('data: ' + data);
//            location.reload(true);
            window.location.replace("/");
             },
        contentType: "application/json",
        dataType: 'json'
    });

})


});




function delete_recipe(recipe_name) {

    console.log("delete");
    $.ajax({
        url: '/api/v1/recipe/'+recipe_name,
        type: 'DELETE',
        success: function(result) {
            console.log(result);
            location.reload(true);
        }
    });

}