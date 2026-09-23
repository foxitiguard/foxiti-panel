<?php
/**
 * phpMyAdmin Access Control - Direct Access Redirect
 * 
 * This file should be placed at /usr/local/FoxitiCP/public/phpmyadmin/index.php
 * to replace the default phpMyAdmin index.php and redirect unauthenticated users
 * to the foxitiPanel login page.
 */

// Check if user is logged into foxitiPanel
session_start();
if (!isset($_SESSION['userID'])) {
    // Redirect to foxitiPanel login page
    header('Location: /base/');
    exit();
}

// If user is authenticated, redirect to the actual phpMyAdmin interface
// through the proper foxitiPanel route
header('Location: /dataBases/phpMyAdmin');
exit();
?>
