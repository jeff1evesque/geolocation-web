/**
* load_logic.js: stores HTML form data into jQuery variables, then determine strongest
*                earthquake within provided 'radius', and 'timeframe', respectively.
*/

$(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var form_data = $('form').serialize();

    $.ajax({
      type: 'POST',
      url: '/json_scraper/',
      data: form_data,
      beforeSend: function() {

      }
    }).done(function(data) {
      console.log( JSON.stringify( data ) );
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });

  });
});
