'use strict';

/**
 * @ngdoc function
 * @name ahglApp.controller:CarouselCtrl
 * @description
 * # CarouselCtrl
 * Controller of the ahglApp
 */
angular.module('ahglApp')
    .controller('CarouselCtrl', function ($scope, carouselSvc, $sce, GamesSvc) {
        $scope.carouselInterval = 5000;
        $scope.slides = [];
        
        var selectedGame = GamesSvc.getSelectedGame();
        carouselSvc.fetchCarousels(selectedGame)
            .then(function(resp) {
                resp.data.results.forEach(function(carousel) {
                    carousel.message = $sce.trustAsHtml(carousel.message);
                    $scope.slides.push(carousel);
                });
            });
    });
