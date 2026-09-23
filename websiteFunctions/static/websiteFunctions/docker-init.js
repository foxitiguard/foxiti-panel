// Wait for Angular to be ready
angular.element(document).ready(function() {
    // Ensure the FoxitiCP module exists
    if (typeof angular.module('FoxitiCP') === 'undefined') {
        console.error('FoxitiCP module not found!');
        return;
    }
    
    // Bootstrap Angular manually if needed
    var element = document.querySelector('[ng-controller="ListDockersitecontainer"]');
    if (element && !angular.element(element).data('$scope')) {
        console.log('Manually bootstrapping Angular for Docker container page');
        angular.bootstrap(element, ['FoxitiCP']);
    }
});