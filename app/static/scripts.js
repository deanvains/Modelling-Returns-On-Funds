$(document).ready(function() {


    /**
     * 
     * 
     * We need to go and hide the fieldsets that we aren't using so that
     * when we select different interest class options it doesn't keep showing
     * residual fields
     * 
     * i.e. we need to do what we are doing for $("#inputDateMonth").change(function(event)
     */
    $("#interestclass").change(function(event) {

        var selected = $("#interestclass").val();

        if (selected == "classE") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();

            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })

            $("#FSProfileOfFundReceipts").show();
            $("#FSInterestRate").show();
            $("#FSAdditionalDonations").show();
            $("#FSRecapitalisation").show();
            $("#FSCapitalDistribution").show();
        }

        if (selected == "classF") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
            $("#FSProfileOfFundReceipts").show();
            $("#FSInterestRate").show();
        }

        if (selected == "classG") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
            $("#FSProfileOfFundReceipts").show();
            $("#FSAdditionalDonations").show();
            $("#FSRecapitalisation").show();
            $("#FSInterestRate").show();
            $("#FSCapitalDistribution").show();
            $("#FSCustomDistribution").show();

        }

        if (selected == "classH") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
            $("#FSSpendingProfile").show();
            $("#FSProfileOfFundReceipts").show();
            $("#FSChangeInSpendingInt").show();
            $("#FSChangeInSpendingMonth").show();
            $("#FSChangeInSpendingYear").show();
            $("#FSInterestRate").show();
        }

        if (selected == "classA") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })

            $("#FSSpendingProfile").show();
            $("#FSProfileOfFundReceipts").show();
            $("#FSChangeInSpendingInt").show();
            $("#FSChangeInSpendingMonth").show();
            $("#FSChangeInSpendingYear").show();
            $("#FSInterestRate").show();
            $("#FSRecapitalisation").show();
            $("#FSCapitalDistribution").show();
        }

        if (selected == "classN") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();

            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
            $("#FSProfileOfFundReceipts").show();
            $("#FSInterestRate").show();
        }

        if (selected == "classQ") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })
            $("#FSProfileOfFundReceipts").show();
            $("#FSInterestRate").show();
        }

        if (selected == "classS") {
            $("#FSOpeningBalance").show();
            $("#FSMonthOrYear").show();


            $("#inputDateMonth").change(function(event) {
                var sel = $("#inputDateMonth").val();
                console.log(sel);
                if (sel == "monthly") {
                    $("#FSStartMonth").show();
                    $("#FSStartYear").hide();
                    //neither is this one
                } else if (sel == "yearly") {
                    $("#FSStartYear").show();
                    $("#FSStartMonth").hide();
                } else {
                    $("#FSStartMonth").hide();
                    $("#FSStartYear").hide();
                }
            })

            $("#FSSpendingProfile").show();
            $("#FSProfileOfFundReceipts").show();
            $("#FSChangeInSpendingInt").show();
            $("#FSChangeInSpendingMonth").show();
            $("#FSChangeInSpendingYear").show();
            $("#FSInterestRate").show();
        }
    })
});

$("#FSCapitalDistribution").show();