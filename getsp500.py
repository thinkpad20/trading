import requests as r
import re

syms = ['mmm', 'abt', 'abbv', 'anf', 'ace', 'acn', 'act', 'adbe', 'adt', 
        'amd', 'aes', 'aet', 'afl', 'a', 'gas', 'apd', 'arg', 'akam', 'aa', 
        'alxn', 'ati', 'agn', 'all', 'altr', 'mo', 'amzn', 'aee', 'aep', 
        'axp', 'aig', 'amt', 'amp', 'abc', 'amgn', 'aph', 'apc', 'adi', 
        'aon', 'apa', 'aiv', 'aapl', 'amat', 'adm', 'aiz', 't', 'adsk', 
        'adp', 'an', 'azo', 'avb', 'avy', 'avp', 'bhi', 'bll', 'bac', 'bk', 
        'bcr', 'bax', 'bbt', 'beam', 'bdx', 'bbby', 'bms', 'brk.b', 'bby', 
        'biib', 'blk', 'hrb', 'bmc', 'ba', 'bwa', 'bxp', 'bsx', 'bmy', 'brcm', 
        'bf.b', 'chrw', 'ca', 'cvc', 'cog', 'cam', 'cpb', 'cof', 'cah', 'cfn', 
        'kmx', 'ccl', 'cat', 'cbg', 'cbs', 'celg', 'cnp', 'ctl', 'cern', 'cf', 
        'schw', 'chk', 'cvx', 'cmg', 'cb', 'ci', 'cinf', 'ctas', 'csco', 'c', 
        'ctxs', 'clf', 'clx', 'cme', 'cms', 'coh', 'ko', 'cce', 'ctsh', 'cl', 
        'cmcsa', 'cma', 'csc', 'cag', 'cop', 'cnx', 'ed', 'stz', 'glw', 
        'cost', 'cov', 'cci', 'csx', 'cmi', 'cvs', 'dhi', 'dhr', 'dri', 'dva', 
        'de', 'dell', 'dlph', 'dnr', 'xray', 'dvn', 'do', 'dtv', 'dfs', 
        'disca', 'dg', 'dltr', 'd', 'dov', 'dow', 'dps', 'dte', 'dd', 'duk', 
        'dnb', 'etfc', 'emn', 'etn', 'ebay', 'ecl', 'eix', 'ew', 'ea', 'emc', 
        'emr', 'esv', 'etr', 'eog', 'eqt', 'efx', 'eqr', 'el', 'exc', 'expe', 
        'expd', 'esrx', 'xom', 'ffiv', 'fdo', 'fast', 'fdx', 'fis', 'fitb', 
        'fslr', 'fe', 'fisv', 'flir', 'fls', 'flr', 'fmc', 'fti', 'f', 'frx', 
        'fosl', 'ben', 'fcx', 'ftr', 'gme', 'gci', 'gps', 'grmn', 'gd', 'ge', 
        'gis', 'gm', 'gpc', 'gnw', 'gild', 'gs', 'gt', 'goog', 'gww', 'hal', 
        'hog', 'har', 'hrs', 'hig', 'has', 'hcp', 'hcn', 'hp', 'hes', 'hpq', 
        'hd', 'hon', 'hrl', 'hsp', 'hst', 'hcbk', 'hum', 'hban', 'itw', 'ir', 
        'teg', 'intc', 'ice', 'ibm', 'iff', 'igt', 'ip', 'ipg', 'intu', 'isrg', 
        'ivz', 'irm', 'jbl', 'jec', 'jdsu', 'jnj', 'jci', 'joy', 'jpm', 'jnpr', 
        'ksu', 'k', 'key', 'kmb', 'kim', 'kmi', 'klac', 'kss', 'krft', 'kr', 
        'ltd', 'lll', 'lh', 'lrcx', 'lm', 'leg', 'len', 'luk', 'life', 'lly', 
        'lnc', 'lltc', 'lmt', 'l', 'lo', 'low', 'lsi', 'lyb', 'mtb', 'mac', 
        'm', 'mro', 'mpc', 'mar', 'mmc', 'mas', 'ma', 'mat', 'mkc', 'mcd', 
        'mhfi', 'mck', 'mjn', 'mwv', 'mdt', 'mrk', 'met', 'mchp', 'mu', 'msft', 
        'molx', 'tap', 'mdlz', 'mon', 'mnst', 'mco', 'ms', 'mos', 'msi', 'mur', 
        'myl', 'nbr', 'ndaq', 'nov', 'ntap', 'nflx', 'nwl', 'nfx', 'nem', 
        'nwsa', 'nee', 'nke', 'ni', 'ne', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc', 
        'nu', 'nrg', 'nue', 'nvda', 'nyx', 'orly', 'oxy', 'omc', 'oke', 'orcl', 
        'oi', 'pcar', 'pll', 'ph', 'pdco', 'payx', 'btu', 'jcp', 'pnr', 'pbct', 
        'pom', 'pep', 'pki', 'prgo', 'petm', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 
        'pxd', 'pbi', 'pcl', 'pnc', 'rl', 'ppg', 'ppl', 'px', 'pcp', 'pcln', 
        'pfg', 'pg', 'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qep', 
        'pwr', 'qcom', 'dgx', 'rrc', 'rtn', 'rht', 'regn', 'rf', 'rsg', 'rai', 
        'rhi', 'rok', 'col', 'rop', 'rost', 'rdc', 'r', 'swy', 'sai', 'crm', 
        'sndk', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw', 'sial', 'spg', 
        'slm', 'sjm', 'sna', 'so', 'luv', 'swn', 'se', 'nlsn', 'stj', 'swk', 
        'spls', 'sbux', 'hot', 'stt', 'srcl', 'syk', 'sti', 'symc', 'syy', 
        'trow', 'tgt', 'tel', 'te', 'thc', 'tdc', 'ter', 'tso', 'txn', 'txt', 
        'hsy', 'trv', 'tmo', 'tif', 'twx', 'twc', 'tjx', 'tmk', 'tss', 'trip', 
        'foxa', 'tsn', 'tyc', 'usb', 'unp', 'unh', 'ups', 'x', 'utx', 'unm', 
        'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn', 'vz', 'viab', 'v', 'vno', 
        'vmc', 'wmt', 'wag', 'dis', 'wpo', 'wm', 'wat', 'wlp', 'wfc', 'wdc', 
        'wu', 'wy', 'whr', 'wfm', 'wmb', 'win', 'wec', 'wpx', 'wyn', 'wynn', 
        'xel', 'xrx', 'xlnx', 'xl', 'xyl', 'yhoo', 'yum', 'zmh', 'zion', 'zts']

def get_sp500_syms(refresh = False):
   if not refresh:
      return syms
   try:
      url = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
      # get html from wikipedia
      raw = r.get(url).content

      # search html for the symbols
      pat = r"(ticker=([a-zA-Z.]+)|symbol/([a-zA-Z.]+))"
      # this will give us a bunch of tuples, we just want the 2nd
      syms_list = []
      for tup in re.findall(pat, raw):
         if len(tup[1]) > 0:
            syms_list.append(tup[1])
         else:
            syms_list.append(tup[2])
      # syms_list = [tup[1] for tup in re.findall(pat, raw)]
      return syms_list
   except Exception as e:
      print "Error when finding symbols:",e
      return []