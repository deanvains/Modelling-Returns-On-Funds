$(document).ready(function() {
    $("#interestclass").change(function(event) {
        if ($("#interestclass").val() == "classE") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#FSMonthOrYear").change(function(event) {
                //this condition not being hit
                if ($("#FSMonthOrYear").val() == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if ($("#FSMonthOrYear").val() == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
        }

        if ($("#interestclass").val() == "classF") {

        }

        if ($("#interestclass").val() == "classG") {


        }

        if ($("#interestclass").val() == "classH") {


        }

        if ($("#interestclass").val() == "classA") {


        }

        if ($("#interestclass").val() == "classN") {


        }

        if ($("#interestclass").val() == "classQ") {


        }

        if ($("#interestclass").val() == "classS") {


        }
    })
});