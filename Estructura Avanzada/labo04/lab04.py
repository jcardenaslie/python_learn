import matplotlib.pyplot as plt
import math, random, time 
import kmp as kmp
import brute_pattern as bp
import numpy as np

# txt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer rhoncus eros arcu, ultrices bibendum elit placerat ut. Vivamus placerat ligula ut ultricies facilisis. Fusce molestie et elit in aliquet. Donec sed ipsum id eros dictum placerat. Nullam tincidunt a justo id facilisis. Sed id lacus luctus, ornare odio ut, ornare odio. Phasellus sed vestibulum nisi. Fusce aliquam facilisis metus vulputate eleifend. Quisque a nunc imperdiet, faucibus lacus sit amet, tincidunt leo. Suspendisse enim arcu, tristique eu ultrices vitae, bibendum vitae nisl. Donec sagittis justo velit, efficitur posuere leo scelerisque eget. Nulla sed enim eleifend orci pharetra interdum. Donec congue, massa non varius mattis, felis mi feugiat neque, non sodales dolor ante porttitor justo. Etiam vestibulum libero ipsum, ornare iaculis velit iaculis ut. Aenean molestie mollis pellentesque.

# Nullam sapien leo, convallis a dui quis, sodales vehicula metus. Nunc libero mauris, pharetra non elit nec, elementum aliquam lorem. Nam egestas nunc id congue congue. Donec in mi sed metus faucibus volutpat sed ac massa. Vivamus euismod nisi vel ipsum sollicitudin, vitae imperdiet tortor euismod. Mauris luctus, nulla eget ornare porttitor, dui lectus pulvinar mi, ac suscipit turpis sem in nunc. Phasellus scelerisque quis diam id pulvinar. Integer dictum nibh mi, quis maximus ligula cursus et. Phasellus justo orci, dictum sit amet pellentesque in, gravida et sapien. Duis lectus augue, semper sit amet velit vel, viverra aliquet tellus.

# Fusce sollicitudin, elit eget accumsan varius, ligula elit sollicitudin orci, in suscipit mauris metus non lorem. Praesent scelerisque est eu nulla porta laoreet. Nunc scelerisque a metus id fermentum. Sed lacinia libero eu varius euismod. Pellentesque molestie augue in lectus viverra, vel interdum orci sagittis. Integer vel nunc nunc. Sed luctus, ex at hendrerit interdum, libero ipsum dignissim elit, eu ullamcorper magna nibh nec mauris. Aliquam at molestie dui. Cras at lectus pulvinar velit faucibus vulputate.

# Pellentesque lacinia ac odio id tempus. Duis eu eros quis augue bibendum blandit. Maecenas pharetra mi risus, eu varius erat tempor nec. Vestibulum placerat sollicitudin ipsum scelerisque egestas. Vestibulum ac diam in nisi fringilla accumsan faucibus at libero. Vestibulum in arcu congue, accumsan nulla sit amet, scelerisque diam. Sed a tortor sem. Integer hendrerit mi vel massa fermentum, at ornare augue sollicitudin. Nullam vel justo vel diam blandit ultrices eget vel ipsum. Aliquam in velit vitae tellus pretium rhoncus vel vitae elit. Etiam odio tellus, porttitor vitae massa eget, porttitor porta ex. In vel dapibus quam. In sodales, ligula vel facilisis egestas, leo nulla volutpat nunc, semper cursus mauris sapien quis velit. Nullam fringilla varius neque, non pellentesque dolor tempus ac.

# Duis fermentum nulla lacus, at ullamcorper nisl tempus eu. Vivamus molestie odio sed velit dapibus hendrerit. Integer vehicula neque vel velit hendrerit, at auctor purus suscipit. Sed gravida in elit quis bibendum. Vivamus sed massa non risus varius venenatis vel ac sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis vulputate, elit et suscipit laoreet, lacus ex cursus quam, a gravida sapien lorem in metus.

# Morbi in velit lacus. Mauris semper laoreet odio ac fringilla. Vestibulum at dapibus libero. Ut vitae turpis ac elit pellentesque accumsan tempus non nibh. Integer laoreet odio leo, hendrerit lobortis ante auctor sit amet. Duis sit amet nisi laoreet augue sagittis vestibulum sit amet at est. Morbi dictum turpis in tellus varius, a porta purus blandit. In ornare eget felis eu tempus. Pellentesque eget tortor nec turpis blandit facilisis a ut ligula. Nunc at mi molestie, viverra sapien in, elementum ligula. Aenean sed ex eget felis rutrum efficitur vitae eu mauris. Sed a quam vel lectus mattis convallis. Phasellus nec elit laoreet metus condimentum porta quis in turpis. Quisque tincidunt vestibulum enim, in luctus lorem bibendum vel.

# Praesent non ex a dui faucibus condimentum. Phasellus et ipsum imperdiet libero gravida consectetur. Cras eleifend purus pulvinar lorem interdum, nec maximus felis eleifend. Curabitur in tincidunt mi. Praesent sit amet bibendum metus. Nullam facilisis arcu et elit dictum tempus. Morbi non luctus felis. Etiam nec placerat diam, ut consectetur justo. Maecenas consequat ante odio, a maximus orci eleifend eget. Ut vitae venenatis arcu. Etiam rhoncus tempus hendrerit. Maecenas accumsan tempor elit nec viverra.

# Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi a nunc arcu. Nulla bibendum eget tortor at consequat. Maecenas sagittis, lorem at suscipit volutpat, odio est tristique mi, at faucibus odio ex et augue. Nulla sit amet maximus leo, nec malesuada diam. Nunc dignissim feugiat euismod. Quisque vel erat et risus mollis iaculis.

# Vestibulum quis feugiat arcu. Maecenas et scelerisque velit. Cras et placerat nisi. Etiam venenatis leo non nisl hendrerit commodo. Mauris sagittis felis a est placerat ornare. In ultricies consequat libero a tempus. Aliquam viverra, urna quis congue mattis, purus ligula tincidunt dui, a efficitur mi diam id lectus. Pellentesque at tempus turpis. Integer malesuada aliquam augue sed euismod. Donec vehicula diam vitae nulla dictum tincidunt. Ut finibus lorem arcu, in pharetra dolor vestibulum et. Nulla consequat ipsum eu lectus consequat elementum. Mauris a pretium purus. Praesent et sodales lorem. Suspendisse malesuada nisi quis est ultrices vestibulum. Sed molestie at velit et lobortis.

# In porttitor est nec gravida porttitor. Nullam id imperdiet augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam interdum dui leo, sed laoreet nisi iaculis ut. Nam non interdum turpis, et lacinia lorem. Donec tincidunt eros in erat mattis tincidunt. Suspendisse laoreet lorem augue, et posuere elit malesuada sed. Nunc vitae vehicula quam. Vivamus egestas, purus in placerat euismod, orci ex congue nisl, consequat eleifend est erat sit amet enim. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vestibulum non magna sapien. Fusce id cursus tellus, vel aliquet ipsum. Phasellus dapibus nibh quis ipsum dictum lobortis. Maecenas et vestibulum lectus. Proin sit amet pretium augue.

# Curabitur cursus porttitor purus, ut accumsan quam accumsan sed. Maecenas neque nulla, tincidunt nec tempus sed, posuere ac ipsum. Etiam quis dapibus orci, a congue dui. Donec id lacinia erat. Ut egestas, ligula et tincidunt efficitur, ex tortor convallis ligula, vel sollicitudin magna lectus eu justo. Integer suscipit mattis rhoncus. Vivamus lobortis, dolor ut cursus ultricies, felis lacus dignissim nisi, porta finibus risus sem vel enim. Suspendisse potenti.

# Suspendisse potenti. Praesent id posuere lacus, in facilisis augue. Suspendisse vehicula suscipit sem, sed interdum velit auctor quis. Suspendisse potenti. Morbi posuere vestibulum dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse orci justo, hendrerit quis laoreet eget, scelerisque sit amet risus. Vivamus a laoreet sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean iaculis efficitur aliquam. Fusce pharetra euismod accumsan.

# Vestibulum scelerisque fringilla sodales. Nullam tempus hendrerit felis, consequat pellentesque lorem viverra eget. Curabitur sed sem molestie, laoreet eros non, porttitor ex. Phasellus aliquam neque at lacus tempor, et congue nulla gravida. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer ut lacinia eros. Proin a scelerisque est, vitae faucibus est. Pellentesque eget pulvinar massa, nec luctus lectus. Suspendisse dictum scelerisque turpis non lacinia. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed scelerisque orci sit amet convallis venenatis. Nunc iaculis quam enim, sit amet fringilla nisl sagittis nec.

# Nam pharetra massa nec magna ultrices interdum. Cras ut nunc at metus elementum imperdiet. Ut vestibulum id lacus in volutpat. Integer at vestibulum quam. Pellentesque pulvinar posuere faucibus. Donec varius lectus eu lorem consequat, at lobortis justo porttitor. Vestibulum blandit quam at scelerisque ornare.

# Donec vehicula elementum velit sit amet sollicitudin. Fusce neque eros, iaculis vel pharetra vel, porttitor et elit. Sed vulputate vitae urna nec congue. Cras rutrum urna erat, quis fringilla arcu lobortis at. Morbi congue sapien nunc, in egestas urna posuere sit amet. Cras dignissim malesuada nunc sit amet ultricies. Donec dictum velit eget diam viverra, eu rutrum ex laoreet. Donec ac pretium lorem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aenean fringilla vehicula tellus, nec pulvinar lectus varius quis. Morbi blandit justo in dolor pretium porttitor. Curabitur imperdiet vel mi vitae lobortis.

# Suspendisse quis arcu nisl. Pellentesque finibus, lectus vitae lacinia imperdiet, dui velit tempus mi, at mattis arcu dui vitae nulla. Mauris auctor suscipit felis, ac consequat tellus dignissim at. Pellentesque porta ullamcorper vulputate. Curabitur consectetur odio consequat mi vestibulum volutpat. Fusce imperdiet, felis et accumsan facilisis, diam turpis consequat erat, sit amet varius est ex sit amet turpis. Aliquam erat volutpat. Vivamus luctus semper elementum. Aenean pretium placerat convallis. Nullam commodo arcu sed mattis sagittis. Donec pharetra, orci et dignissim mollis, tellus lorem finibus enim, eu porttitor lacus felis eu quam. Pellentesque vulputate imperdiet tellus at lacinia.

# Nam fringilla neque felis, et rutrum leo suscipit at. Praesent venenatis in ligula quis ornare. Quisque congue mi in tristique facilisis. In hac habitasse platea dictumst. Suspendisse tellus nisl, malesuada vitae tincidunt a, consequat sed enim. Vestibulum cursus ullamcorper tincidunt. Vestibulum eget justo placerat, varius nunc vel, cursus nulla.

# Phasellus viverra urna a nisl tristique, eu fermentum mi fermentum. Nam turpis nulla, semper at magna ut, tincidunt vulputate est. Morbi vitae semper diam. Vestibulum imperdiet efficitur odio. Proin nec ornare diam, a malesuada sem. Nunc neque justo, fringilla id ipsum ac, egestas semper sem. Sed elementum at turpis vel consequat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec bibendum id nisi eget tincidunt. Proin mi odio, luctus at pharetra nec, tristique a augue.

# Ut egestas auctor nunc ac porta. Sed dolor justo, porttitor in lobortis sit amet, dapibus a ante. Fusce eros sem, tristique eget blandit sed, euismod egestas felis. Aenean elementum varius lacus, sit amet scelerisque risus viverra sed. Integer eu commodo elit. Suspendisse a porttitor magna, vitae volutpat ante. Suspendisse non suscipit neque, quis tempus massa. In convallis tellus eget leo luctus vestibulum. Curabitur nec dapibus eros. Morbi aliquam lacus eget viverra lobortis. Etiam eleifend cursus lacus, eget blandit eros pretium ac. Suspendisse at urna non libero iaculis pellentesque eu non massa. Nullam aliquam aliquam scelerisque. Quisque erat lacus, pretium tempus pretium a, posuere eu leo.

# Curabitur dapibus diam sit amet mollis luctus. Aliquam pellentesque magna dapibus rutrum porta. In sed semper lacus. Nullam sit amet lobortis magna. Morbi quis aliquam mauris. Sed vel dui nunc. Integer id nulla ut est ornare semper ut ac tortor. Nunc et sem sem. Nullam scelerisque, elit gravida commodo rhoncus, risus nunc iaculis diam, sed mattis erat odio vitae sem. Maecenas sed sem nec risus faucibus facilisis eget pulvinar magna. Mauris efficitur, turpis nec cursus lacinia, ipsum nisl mollis arcu, vitae pulvinar purus felis ut nulla. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras tristique vitae nulla vitae pellentesque.

# Sed eu dolor at velit interdum condimentum sit amet eget massa. Nulla ultrices leo ac sem gravida tincidunt. Etiam magna risus, vestibulum a enim in, maximus luctus dolor. Donec erat lorem, faucibus eu purus sit amet, lacinia suscipit leo. Donec at ipsum odio. Phasellus ornare sodales neque, efficitur pulvinar ligula posuere eget. Vivamus ultrices aliquet mollis. Nulla placerat pellentesque orci, id mattis dolor egestas eget. Nullam interdum justo ac turpis feugiat, vel semper erat rhoncus.

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus quis est tincidunt, congue lectus ac, elementum lorem. Aenean est dolor, tempus eu arcu quis, eleifend aliquet odio. Vestibulum a fermentum enim. Etiam commodo odio in volutpat porta. Sed pharetra sapien nisi, eu placerat nulla vehicula in. Vestibulum euismod rutrum ipsum eget iaculis.

# Pellentesque molestie pretium aliquet. Quisque a neque sed nisl facilisis feugiat vitae sit amet metus. Suspendisse a massa est. Sed venenatis leo vitae gravida elementum. Donec euismod, leo a tincidunt finibus, ligula nulla bibendum leo, non sagittis leo sapien nec mauris. Donec rutrum nisi ante, sit amet sodales nunc maximus at. Sed dictum maximus tempus. Pellentesque ac quam id urna scelerisque pharetra sed vehicula odio. Integer ullamcorper imperdiet massa, gravida tincidunt felis scelerisque non. Phasellus sit amet arcu tellus. Vestibulum venenatis, ex sed pellentesque rutrum, ante eros interdum ante, nec egestas justo nibh vitae eros.

# Nunc sem augue, dapibus sit amet tincidunt in, maximus ac justo. Nam eros nunc, iaculis a ultricies at, blandit nec velit. Proin id efficitur nisl, quis dignissim dui. Praesent ut ornare quam, sed efficitur purus. Quisque dolor nisi, congue nec pulvinar sed, bibendum eget nisl. Morbi non erat egestas, vulputate magna at, sodales mi. Suspendisse potenti. In consectetur ligula ligula, sed facilisis sem euismod id. Fusce massa neque, feugiat et fermentum ut, semper in nisl. Nullam maximus commodo nibh, sit amet condimentum elit sollicitudin eget. Donec at magna tempor, vulputate quam id, elementum libero.

# Morbi accumsan diam at enim dictum, in laoreet nisl finibus. Fusce eu dolor nunc. Nam ultrices gravida risus vel ultricies. Nulla rutrum iaculis ligula, eu convallis elit sagittis egestas. Donec nisl nisl, vulputate ac porta vel, ultrices et nibh. Proin cursus luctus interdum. In eget ex magna.

# In metus nunc, viverra ac mi sed, imperdiet imperdiet arcu. Praesent varius blandit arcu sed porttitor. Morbi non felis lectus. Etiam vel posuere eros. Mauris nibh quam, consectetur in dui vel, dignissim malesuada sem. Suspendisse interdum mauris arcu, eget suscipit lorem feugiat ac. Aliquam facilisis nunc a blandit mattis. Sed ac sem turpis. Proin id odio nec metus rhoncus rhoncus sit amet dignissim arcu. Mauris egestas sollicitudin pharetra. Ut imperdiet, turpis in malesuada vehicula, magna odio hendrerit lorem, vel elementum risus felis ac sem. Nulla eget nunc sapien. Nullam odio justo, pharetra non leo sed, accumsan dictum arcu. Nullam vel egestas augue. Morbi porta rutrum fringilla. In viverra volutpat nunc at venenatis.

# Vivamus euismod maximus tristique. Sed hendrerit felis et sapien porttitor, ac aliquet lacus commodo. Nunc ex nisi, hendrerit a nibh in, condimentum commodo nisi. Fusce auctor dui dictum eros condimentum imperdiet. In hac habitasse platea dictumst. Donec aliquam metus porttitor odio maximus lacinia. Donec dictum gravida odio, id maximus nisl ullamcorper sit amet. Proin consectetur aliquet orci, a luctus mi faucibus eget. Vestibulum ullamcorper imperdiet nisl vitae vulputate. Nunc ligula diam, vehicula a consectetur et, elementum a dui. In hac habitasse platea dictumst.

# Aliquam et placerat nisl, in sollicitudin felis. Duis vitae faucibus risus, quis cursus massa. Ut fermentum felis nibh, et pellentesque arcu sollicitudin eu. Mauris pulvinar commodo vulputate. Sed magna quam, lobortis ut consequat ut, ultricies sed ligula. Cras eu volutpat velit, eget ultricies velit. Cras vitae ligula dapibus, cursus velit in, finibus dolor. Ut nisi quam, molestie nec rhoncus finibus, fringilla vel lectus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

# Sed pulvinar eros et placerat vehicula. Vivamus mollis blandit tincidunt. Proin accumsan id dolor eu consectetur. Sed eget dolor velit. Phasellus vel lacus sed ipsum laoreet ultricies. Integer varius sem dui, at tincidunt lectus placerat in. Quisque lorem nisl, ullamcorper vel faucibus sit amet, feugiat ut metus. Aliquam egestas metus ac quam aliquet vehicula. Maecenas eu mauris nisi. Morbi et ex est. Aliquam lacinia sed odio ac rhoncus. Vestibulum massa erat, euismod nec quam sed, dignissim facilisis lectus. Nulla vitae est sit amet neque commodo aliquet et at sem. Vestibulum metus orci, vestibulum ut dapibus eleifend, laoreet id mi. Aliquam sodales diam tortor, nec vulputate elit maximus nec.

# Nullam imperdiet maximus quam quis sagittis. Mauris sed aliquet sapien. Integer turpis felis, lobortis quis nunc at, fermentum interdum lorem. Pellentesque quis nulla volutpat, fermentum orci ut, congue ex. Donec lobortis lectus sit amet euismod lobortis. Aenean libero lorem, fermentum nec justo quis, elementum lobortis ipsum. Aenean et neque imperdiet lorem mollis blandit ut pharetra velit. Aliquam in sem blandit, consectetur nisl id, consectetur urna. Nunc malesuada non elit id interdum. Aliquam sodales, ipsum vitae interdum luctus, lacus dui lobortis nisl, sed egestas est arcu at neque.

# Nullam eget orci quis libero maximus sagittis id nec lorem. Etiam mauris nisl, ornare vel eleifend at, dictum vel magna. Donec ut tortor nec neque lobortis volutpat. Nullam lorem sapien, pulvinar dapibus lorem nec, porta porttitor purus. Aenean cursus eros a ligula viverra, at tincidunt tellus hendrerit. Aenean bibendum vulputate lectus, vel pharetra elit vehicula non. Aliquam non vehicula ex. Nulla rutrum, justo vel molestie facilisis, mi urna maximus ante, vel lobortis diam lorem non massa. Fusce a ipsum hendrerit, maximus nisl eget, interdum mauris. Maecenas tincidunt lobortis urna vel ullamcorper. Aliquam iaculis commodo nisl sit amet ullamcorper. In ac arcu non diam placerat sodales. Mauris velit nibh, consequat eget dolor at, lacinia pulvinar mauris. Mauris at nisl viverra, egestas libero nec, dictum sapien. Donec nec luctus dolor, vel dapibus mauris.

# Pellentesque pellentesque nibh vel urna ultrices pulvinar. Maecenas quis molestie nibh. Vestibulum efficitur odio vel leo porttitor mattis. Aliquam eget lorem viverra, commodo mauris nec, placerat dolor. Fusce urna urna, bibendum sed sapien vel, scelerisque rhoncus purus. Nulla rutrum elit a libero condimentum, ac porta nisi mattis. Nullam orci turpis, sagittis quis urna nec, gravida molestie velit. Nunc id felis euismod leo viverra tincidunt ut eu orci. Vivamus ultricies tincidunt arcu sit amet aliquet. Sed vel purus libero. Integer non lectus in magna fringilla volutpat eu ut lectus. Nulla sit amet nisl in tortor interdum vestibulum. Nulla leo mi, volutpat quis lacinia eu, luctus a justo. Etiam a purus cursus, tincidunt tortor in, condimentum lacus. Integer sed sollicitudin nunc, et accumsan leo. Donec non facilisis massa.

# Cras elementum tincidunt orci quis pulvinar. Ut imperdiet dolor elit, id molestie ligula pellentesque eu. Duis sit amet vestibulum dui, vitae efficitur risus. Maecenas vitae orci dictum, gravida turpis ut, auctor nulla. Aliquam tincidunt aliquet ultrices. Nullam pharetra sed sem quis eleifend. Proin sodales lorem orci. Etiam iaculis commodo vehicula. Fusce nec massa odio. Mauris molestie ultrices mattis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras molestie sit amet dui in rhoncus. Donec ac nisi ornare, semper ligula vitae, molestie massa. Vestibulum pretium, nibh ultricies lacinia molestie, sem mi scelerisque lectus, et fermentum neque odio a orci. Quisque aliquet a tortor nec malesuada. Suspendisse egestas mi metus, in iaculis nisi tristique ut.

# Nulla bibendum, lorem vel finibus eleifend, urna magna iaculis libero, vel tincidunt elit erat sit amet nunc. Nam et elementum tellus, in bibendum velit. Aliquam pulvinar auctor arcu, id faucibus nisi malesuada id. Maecenas varius hendrerit dolor, eget faucibus tortor vulputate eget. Vestibulum scelerisque tristique justo. Cras neque erat, tristique vel varius vitae, lacinia a elit. Sed in enim venenatis, accumsan nibh at, convallis urna. Vivamus efficitur tortor ligula, quis vehicula lorem egestas sed. Proin sit amet efficitur nibh. Cras tristique in lorem nec semper. Morbi sit amet augue pulvinar, feugiat arcu at, eleifend metus. Suspendisse imperdiet sit amet felis at vulputate. Praesent vulputate non lectus non tristique. Sed ac lobortis odio, at interdum urna.

# Aliquam eget risus ex. Aenean non dignissim enim. Nunc facilisis porta dignissim. Pellentesque dignissim egestas turpis vel egestas. Praesent rutrum porttitor pharetra. Cras aliquet sagittis egestas. Curabitur porta purus quis semper efficitur. Aenean suscipit ultrices ligula, a tincidunt mi tempor at. Ut purus nibh, imperdiet sit amet ligula id, pellentesque consequat augue. Pellentesque congue vehicula ex, quis lobortis arcu aliquet vel. Proin interdum, turpis ut tempus euismod, turpis neque venenatis nisi, non molestie metus odio nec enim. Sed vitae velit nulla. Nulla scelerisque arcu velit, blandit consequat ipsum pharetra sit amet. Etiam vel tempus neque.

# Integer ut congue quam. Nullam tristique gravida urna. Quisque commodo aliquet ante et tincidunt. Vivamus sit amet ultrices mi. Etiam mattis malesuada mollis. In justo ex, rhoncus vel lectus sit amet, rhoncus vestibulum sapien. Donec est neque, eleifend vitae fringilla in, tristique sit amet turpis. Aenean eros felis, commodo sit amet nulla vel, ullamcorper posuere sapien. Praesent fermentum facilisis purus, sed congue dolor luctus eget. Fusce a malesuada mauris.

# Fusce consequat lacus erat, non commodo sapien cursus et. Pellentesque molestie justo vel mi varius tempus. Maecenas eleifend volutpat vehicula. Suspendisse lacus ante, lacinia ut lacus et, eleifend ultricies lectus. Nam consequat ex at sagittis ornare. Vivamus facilisis sed elit rhoncus gravida. Nunc ornare, diam eu porttitor blandit, dui tortor posuere leo, quis faucibus lorem ex et nisl. Proin vel tempor mauris. Aliquam egestas, justo in suscipit mollis, urna risus luctus enim, eget viverra mauris enim at tellus. Nulla porttitor accumsan sodales. Etiam a orci lacus.

# Ut et nunc ut velit egestas placerat in ut dui. Mauris tempus dui vel lectus varius vulputate. Donec viverra est ipsum, ut porttitor augue pulvinar eu. Sed lobortis ligula vel neque tristique iaculis. Nullam dignissim et magna id eleifend. Duis sed metus lacus. Phasellus pretium, velit ac molestie elementum, quam nisi auctor tortor, quis fermentum eros mi eu lectus. Aenean et nunc et ante congue condimentum vitae eu nisl. Morbi ultricies, diam at porta porta, mi quam bibendum eros, nec congue sapien leo a justo. Duis neque dolor, pharetra at hendrerit pulvinar, sagittis eget magna. Nam facilisis mattis dapibus. Fusce magna felis, dictum molestie venenatis ut, rhoncus eget lorem. Phasellus non massa egestas, efficitur enim eget, varius dui. Cras vitae rutrum lectus, ac tincidunt dui.

# Praesent scelerisque bibendum varius. Quisque laoreet dolor urna, et tempus nulla accumsan vitae. Phasellus lobortis placerat urna, et aliquet enim ornare non. Nunc nec metus at sapien molestie tincidunt. Vivamus auctor velit in condimentum lobortis. Praesent non sem nisi. Sed sed velit in dolor viverra gravida. Ut vulputate massa diam, facilisis dapibus est suscipit in. Vestibulum vulputate arcu a felis auctor dictum. Quisque cursus tellus a aliquam aliquet. Sed sollicitudin fermentum enim quis sagittis. Nullam ultricies molestie dui vitae vestibulum. Sed sit amet lectus nec ipsum ultricies malesuada. Morbi in massa in diam fringilla facilisis eu condimentum mi. Pellentesque blandit condimentum libero, sed fringilla nulla dignissim a.

# Nullam posuere diam ac ultricies consequat. Nullam tincidunt porttitor tortor a pellentesque. In lacinia, nunc et tincidunt ullamcorper, est ex elementum nibh, at sagittis libero nibh et justo. Nullam eget ante tellus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam eget ipsum semper, accumsan ex non, blandit leo. Vivamus tempor eros consectetur purus porta, eu elementum elit iaculis. Sed eu scelerisque augue. Morbi aliquet arcu purus, quis vestibulum tortor sodales eget. Etiam euismod lorem ac nunc sagittis dapibus. Donec in urna vitae sapien bibendum eleifend."""

# pat = "dictum"


def kmp_time():
	start = time.clock()
	kmp.KMPSearch(pat,txt)
	end = time.clock()
	result = end - start
	return result

def brute_time():
	start = time.clock()
	bp.brute_pattern(pat,txt)
	end = time.clock()
	result = end - start
	return result

test_size = [10, 100, 1000, 10000, 100000, 1000000]


kmp_times = []
brute_times = []

for j in test_size:
	pat = "bla"
	txt = pat*j

	kmp_mean = 0
	brute_mean = 0
	for i in range(0,5):
		kmp_mean +=kmp_time()
		brute_mean +=brute_time()
	kmp_times.append(kmp_mean/5)
	brute_times.append(brute_mean/5)

plot = []
kmp_np = np.array(kmp_times)
plt.plot([1,2,3,4,5,6],kmp_times)
plt.plot([1,2,3,4,5,6],brute_times)

# plt.show()
plt.title('String Pattern algorithms')

plt.ylabel('Tiempo (s)')
plt.xlabel('pattern size * (10^n)')
plt.legend([
	'KMP',
	'Brute Force'
	], loc='upper left')
plt.show()