"use strict"

var app = angular.module('myApp', ['nya.bootstrap.select']);

app.controller('getController', function($scope, $http){
    $scope.dados = null;
    $http({
        method: 'GET',
        url:"",
        headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(function successCallback(response){
        $scope.dados = response.data
    }); 
})