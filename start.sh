#!/bin/bash
service supervisor start &
service supervisor reload &
service supervisor status &
service apache2 start &
service apache2 restart &
service apache2 status 