<?php

use Illuminate\Support\Facades\Route;

Route::get('/employees', [EmployeeController::class, 'index']);
