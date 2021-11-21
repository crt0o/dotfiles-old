/* user and group to drop privileges to */
static const char *user  = "nobody";
static const char *group = "nobody";

// Changed this so the color doesn't change when typing and if password is wrong
static const char *colorname[NUMCOLS] = {
	[INIT] =   "black",     /* after initialization */
	[INPUT] =  "black",   /* during input */
	[FAILED] = "black",   /* wrong password */
};

/* treat a cleared input like a wrong password (color) */
static const int failonclear = 1;
