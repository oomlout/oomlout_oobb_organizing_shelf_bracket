$fn = 50;


difference() {
	union() {
		translate(v = [0, 24.0000000000, 0]) {
			hull() {
				translate(v = [-32.0000000000, 11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [32.0000000000, 11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-32.0000000000, -11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [32.0000000000, -11.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
		translate(v = [-30.0000000000, 0, 0]) {
			hull() {
				translate(v = [-2.0000000000, 17.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [2.0000000000, 17.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-2.0000000000, -17.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [2.0000000000, -17.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
		rotate(a = [0, 0, 26.5650511771]) {
			hull() {
				translate(v = [-33.0410196625, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [33.0410196625, 2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [-33.0410196625, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
				translate(v = [33.0410196625, -2.0000000000, 0]) {
					cylinder(h = 14, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-23.0000000000, -15.0000000000, 7.0000000000]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#cylinder(h = 250, r = 5.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.7500000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-23.0000000000, 0.0000000000, 7.0000000000]) {
			rotate(a = [0, 90, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.7500000000, r2 = 5.5000000000);
						}
						#cylinder(h = 250, r = 5.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.7500000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [15.0000000000, 31.5000000000, 14.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.3750000000, r2 = 4.5000000000);
						}
						#cylinder(h = 250, r = 4.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.3750000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-15.0000000000, 31.5000000000, 14.0000000000]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
						#translate(v = [0, 0, -4.2000000000]) {
							cylinder(h = 4.2000000000, r1 = 2.3750000000, r2 = 4.5000000000);
						}
						#cylinder(h = 250, r = 4.5000000000);
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.3750000000);
						}
						#translate(v = [0, 0, -14.0000000000]) {
							cylinder(h = 14, r = 2.2500000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-37.0000000000, 22.5000000000, 0]) {
			cube(size = [74, 18, 11]);
		}
	}
}