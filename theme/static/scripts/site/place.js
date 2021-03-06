define(['jquery', 'bootstrap', 'chroma'], function($, bootstrap, chroma) {

    var colorSteps = ['#7ab800', '#edcf3b', '#ff0000'],
        colorScale = chroma.scale(colorSteps).domain([0, 100]),
        $placeOpeness = $('.place-openness'),
        $datasetOpeness = $('.dataset-openness'),
        naString = 'n/a',
        score;

    function initializePlace() {

        $.each($placeOpeness, function(index, el) {
            var $el = $(el);
            if ($el.data('score') === naString) {
                $el.css({
                    'background-color': 'grey',
                    'color': 'white'
                });
            } else {
                score = parseInt($el.data('score'), 10);
                $el.css({
                  'background-color': colorScale(score).hex(),
                  'color': 'white'
                });
            }
        });

        $.each($datasetOpeness, function(index, el) {
            var $el = $(el);
            if ($el.data('score') === naString) {
                $el.css({
                    'background-color': 'grey',
                    'color': 'white'
                });
            } else {
                score = parseInt($el.data('score'), 10);
                $el.css({
                  'background-color': colorScale(score).hex(),
                  'color': 'white'
                });
            }
        });

    }

    return {
        init: initializePlace,
    };

});
