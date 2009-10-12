$(document).ready(function() {
    $('#id_day').datepicker({
        dateFormat: 'yy-mm-dd',
        defaultDate: 0,
        firstDay: 1
    });
    
    $('form#payment').submit(function() {
        var amount = $('#id_amount').val();
        var to_pay = parseInt($('#to_pay').text(), 10);
        if (!amount.match(/^\d+$/)) return false;
        if (amount % 5) {
            alert('Please pay only amounts that are dividable by 5. ' + amount + ' is not.');
            return false;
        }
        if (amount > to_pay) {
            alert('That\'s more money than you have to pay. Paying in advance is not possible yet.');
            return false;
        }
    });
});